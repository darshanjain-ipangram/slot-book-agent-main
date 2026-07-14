from decouple import config

#groq 
GROQ_API_KEY = config("GROQ_API_KEY")
GROQ_MODEL_NAME = config("GROQ_MODEL_NAME",default="llama-3.3-70b-versatile")

#cal.com
CALCOM_KEY = config("CALCOM_KEY")
CALCOM_EVENT = config("CALCOM_EVENT")