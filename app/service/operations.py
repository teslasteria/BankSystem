from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repository import wallets as wallets_repository
from app.schemas import OperationRequest


def add_income(db: Session, operation: OperationRequest):

    if not wallets_repository.is_wallet_exist(db, operation.wallet_name):
        raise HTTPException(
            status_code=404,
            detail=f'Wallet {operation.wallet_name} not found',
        )

    wallet = wallets_repository.add_income(
        db, operation.wallet_name, operation.amount
    )

    db.commit()
    db.refresh(wallet)

    return {
        'message': 'Income added',
        'wallet': operation.wallet_name,
        'amount': operation.amount,
        'description': operation.description,
        'new_balance': wallet.balance,
    }


def add_expence(db: Session, operation: OperationRequest):
 
    if not wallets_repository.is_wallet_exist(db, operation.wallet_name):
        raise HTTPException(
            status_code=404,
            detail=f'Wallet {operation.wallet_name} not found',
        )

    if operation.amount <= 0:
        raise HTTPException(
            status_code=400,
            detail=f'Amount {operation.amount} should be greater than 0',
        )

    wallet = wallets_repository.get_wallet_balance_by_name(
        db, operation.wallet_name
    )
    if wallet.balance < operation.amount:
        raise HTTPException(
            status_code=400,
            detail=f'Insufficient funds. Available: {wallet.balance}',
        )

    wallet = wallets_repository.add_expense(
        db, operation.wallet_name, operation.amount
    )

    db.commit()
    db.refresh(wallet)

    return {
        'message': 'Expense added',
        'wallet': operation.wallet_name,
        'amount': operation.amount,
        'description': operation.description,
        'new_balance': wallet.balance,
    }
