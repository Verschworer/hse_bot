import turicreate as tc

model = tc.load_model('model_fake_or_real')


example_text = dict(
                    title=["Putin is going to take over the world, who would have thought ?!"],
                    text=["As we were recently told, Russian President Vladimir Putin is going "
                          "to take over the world using weapons of mass destruction, in addition "
                          "he is going to use a group of Russian hackers who will penetrate into "
                          "the nights of Americans and secretly vote for President Donald Trump"]
                    )


example_prediction = model.classify(tc.SFrame(example_text))
print(example_prediction, flush=True)
