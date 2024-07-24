from flask import Blueprint, render_template, request, redirect, url_for
from user import register_user
from authority import Authority, CertificateRepository
from communication import Communication

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        # Handle encryption
        pass
    return render_template('encrypt.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        user_data = register_user(email)
        return render_template('register.html', user_data=user_data)
    return render_template('register.html')

@bp.route('/sign', methods=['GET', 'POST'])
def sign():
    if request.method == 'POST':
        email = request.form['email']
        authority = Authority()
        user_data = register_user(email)
        certificate, signature = authority.sign_certificate(user_data)
        return render_template('sign.html', certificate=certificate, signature=signature)
    return render_template('sign.html')

@bp.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        email = request.form['email']
        certificate = request.form['certificate']
        signature = request.form['signature']
        authority = Authority()
        is_valid = authority.verify_certificate(email, certificate, signature)
        return render_template('verify.html', is_valid=is_valid)
    return render_template('verify.html')

@bp.route('/async', methods=['GET', 'POST'])
def async_communication():
    if request.method == 'POST':
        communication = Communication()
        message = request.form['message']
        encrypted_message = communication.send_message(message)
        return render_template('async.html', encrypted_message=encrypted_message)
    return render_template('async.html')

@bp.route('/proof', methods=['GET', 'POST'])
def proof():
    if request.method == 'POST':
        # Handle proof of knowledge
        pass
    return render_template('proof.html')