from jose import jwt, JWTError

SECRET_KEY = "KlgH6AzYDeZeGwD288to79I3vTHT8wp7"
ALGORITHM = "HS256"

jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])