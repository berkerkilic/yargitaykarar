import fasttext

model = fasttext.train_supervised(input='kararegitimtam.csv', autotuneValidationFile='karartest1.csv')
