from passlib.context import CryptContext
context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=50000
)

App_secret_key = "qrljuoezyihwmpxv"
email_id = "neofisheries@gmail.com"