import fasttext

model = fasttext.train_supervised(input='kararegitim4.csv', 
                                  autotuneValidationFile='karartest4.csv', 
                                  autotuneDuration=60)
model.save_model("modelkarar4.bin")

