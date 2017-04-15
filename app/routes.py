from flask import jsonify, request
from app import app
from app.common import common
from app.models import Users

class Api():
    @app.route('/test')
    def test():
        return jsonify(common.trueReturn('aa', "提示"))


    @app.route('/users', methods=['GET'])
    def getAll():
        users = Users.getAll(Users)
        data = []
        for user in users:
            data.append({
                'id': user.id,
                'email': user.email,
                'username': user.username,
                'login_time': user.login_time
            })
        return jsonify(common.trueReturn(data, "提示"))


    @app.route('/user', methods=['POST'])
    def add():
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        # 最后一条记录及其ID
        lastUserRecord = Users.query.order_by('-id').first()
        if (lastUserRecord is None):
            newRecordId = 1
        else:
            newRecordId = lastUserRecord.id + 1

        user = Users(id=newRecordId, email=email, username=username, password=password)
        Users.add(Users, user)

        userInfo = Users.get(Users, user.id)
        if userInfo:
            returnUser = {
                'id': userInfo.id,
                'username': userInfo.username,
                'email': userInfo.email,
                'login_time': userInfo.login_time
            }
            return jsonify(common.trueReturn(returnUser, "用户注册成功"))
        else:
            return jsonify(common.falseReturn('', '用户注册失败'))


    @app.route('/user/<int:id>', methods=['GET'])
    def get(id):
        """
        获取用户信息
        :return: json
        """
        user = Users.get(Users, id)
        if not user:
            result = common.falseReturn('', '找不到用户')
        else:    
            returnUser = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'login_time': user.login_time
            }
            result = common.trueReturn(returnUser, "请求成功")
        return jsonify(result)


    @app.route('/user/<int:id>', methods=['PUT'])
    def update(id):
        """
        修改用户信息
        :return: json
        """
        # 获取请求的数据
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        user = Users.get(Users, id)

        if (user is None):
            result = common.falseReturn('', '找不到要修改的记录')
        else:
            user.username = username
            user.password = password
            user.email = email

            Users.update(Users)

            result = common.trueReturn({'id': user.id, 'username': user.username, 'password': user.password, 'email': user.email, 'login_time': user.login_time}, '请求成功')

        return jsonify(result)


    @app.route('/user/<int:id>', methods=['DELETE'])
    def delete(id):
        """
        删除用户信息
        :return: json
        """
        Users.delete(Users, id)
        return jsonify(common.trueReturn('', '删除成功'))


