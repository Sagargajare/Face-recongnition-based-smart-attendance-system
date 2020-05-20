import pyrebase

config ={
  "type": "service_account",
  "project_id": "smart-attendance-system-26042",
  "private_key_id": "a3c1bf7fc5f08e2f77c748c5c68aaa38d642834f",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCvGpAzv26oyXD+\nCGA+ttOfv10R7mUvsLusziqEUJJCFCVlXmag7XcY+9BB3Y8FgrW4p/6pKTOeyJ4T\nmGUzcY5X4ShWQvMHKkwP0/I5gUaz5U3x2r6bPMSFn1nMEhIL3aPVFzdUpAIvP82E\noWKUC0T++91sBhIcPeLi6Xv5NbzsJbfNF2PhO0BaasV5tqBIO6/edW6NnE4R2AFr\ng5u0vyk8fYrAXy8TtpU7wmXPeg8D3swfX/xvAa/QwTNCtRHNO1YnVX8fsyX+tUU0\n1O6Uv0E2WNSkFge+ESL630hYn2RkiiL1r30GETMaECcgUi7lcNDPOieSZoe+FKuG\n8I6ySdEBAgMBAAECggEAMIoFhULAsys8Fj9OJrRZj4Plkc3q4MB2Fd4ErS8EjCq3\nfxUfD+cjx5ouTcPUHKvyIeD31/6i35YvM7FgBFWrJrM0kkz2v3q7IPwYvlYWulGL\nPMrtYW0D8SKOKuKre/yRqMVJwj3AmUZvex+divpgwuogpAw+wvNozIv6oMeDulX3\nzwgml1QUlqPP19sQj/C3+/2nslLgLvMKSgGCXo2yMx/WDaZFvYMiN55yqzSWo2HV\nGUOCMTn/kNOa6VJfR9uFXiyLW5cwMlEgZsJB0TCmY8TP79dzEImmcRVPQs6nvJKn\nfBTSYhqucJQ/Nqa5eGr/rIYdvIu7cKuITeuJfrkPnQKBgQDzHYZ7DnFv76McAOgN\nuJ8XZht1/4FtKTYz6a7Vrn1ppRAMnyjL/1a0XPlgtR2jmcTAAWVzaCP4QJaRm1Yr\n9sMjcUGUnOiYoxENT2Z5zsPLkdPgHgpheDRa85s/u5uDeQ+UO90+hG8cuGv/MV6i\nx7FILhKKnPgHB4KJBySuWEZYlwKBgQC4Ykn20tXSPSVkSZLVMxVDFG8OYhM7241P\ndUrlrEu+JILaVmrUfar5yZirAcSLNIwnRSFdbnbIG+jMu4R8QtmUxzba/ojx+mfa\nuZVlmskIM8jdvhiSnY7JCFqzteNG/s6HImAx+udPrHivynSNm57sumGm+4bTK73u\nc/Y3Jsh+JwKBgQDQKeDDLxu8P5EG4lPPo9w82cX7pBn7EQWDL7zu4+godBgo5oK1\nIV3pM46n2oyVT42i5c8rIOljoFIMPNhs7m4pw8jmae/S+hUYs3rII12MycGELdSv\nnpAdrGarDIVc7mSDhTqsVBMboWF/cZNZh+jpJ+HiZAMPacPAdqhWy+j34wKBgGKT\nufOKGOMD6d/KLgRqAS4R2KYZ7SqNYOlgTiCokv4fSw4sMYVVgnl1PHgAw/GgsGW2\nYfYvvrWRpk7+2gANRYJzV3KRrumf9LJNkf/2VxBZj0RuA3kvX00/eC6oSdCFHinF\nSSSvfcds8EEbvmCPGNJ7ewXpZ9WyhyLbQIGP7JT1AoGAJjs5tojyQC3bcK/5uoV0\nQYDZkIRLu/RZ4YBgtZc94pZhlGFNI4Hqli1Ur4cum+qUPOv8Se0FSoD5920DdaUn\nQdnulmwUd8CrVoQ8DdoC+NslMiRsDQoPUvSle3RK0U6cEpGlvXbpDTlUvUIQeYuR\nmG0Re9MSwekqLuQnCN87Cpw=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-cpcjy@smart-attendance-system-26042.iam.gserviceaccount.com",
  "client_id": "101603139283184607937",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-cpcjy%40smart-attendance-system-26042.iam.gserviceaccount.com"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud = 'attendance/filname_on_firestore'
path_local = 'local_file_path'
storage.child(path_on_cloud).put(path_local)

#storage.child(path_on_cloud).download('test_download.jpg')
