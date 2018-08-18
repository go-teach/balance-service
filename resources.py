from flask import request
from flask_restful import Resource, reqparse
from models import BalanceModel


class BalanceCreate(Resource):
    def post(self):        
        new_balance = BalanceModel(
            username = request.form['username'],
            amount = 0
        )
        try:
            new_balance.save_to_db()
            return {'message': 'Balance for {} was created'.format(new_balance.username) }
        except Exception as e:
            return {'message': 'Something went wrong'}, 500


class BalanceUser(Resource):
    def get(self, username):
        balance = BalanceModel.query.filter_by(username = username).first()
        
        if balance:
            return {'username': balance.username,
                    'amount': balance.amount}
        else:
            return {'message': 'Balance not found'}, 404


class BalanceUserAdd(Resource):
    def post(self, username):
        amount = int(request.form['amount'])
        balance = BalanceModel.query.filter_by(username = username).first()
        balance.add(amount)
        return {'status': 'OK'}


class BalanceUserCharge(Resource):
    def post(self, username):
        amount = int(request.form['amount'])
        balance = BalanceModel.query.filter_by(username = username).first()
        balance.charge(amount)
        return {'status': 'OK'}
