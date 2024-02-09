
# Friend or foe?

A brief solution of how to solve this challenge which was given in ISTE and MIST Aurora CTF.


## Solution

This challenge is based off a new injection techniques, i.e, prompt injections. The player is given access to a discord server which has a bot with the name `sudo.Aura`. This bot has the uses an open source Llama AI model, `dolphin-2.0-mistral-7B-GGUF`.

The Llama AI models can be manipulated using the ethical reasoning methods like `do <a task> to save <something>`. You will know that the injection is working when you get same replies repeatedly.

![breakdown](https://cdn.discordapp.com/attachments/1196101538104475749/1205199151428796487/2024-02-08T2240269988700760530.png?ex=65d7802d&is=65c50b2d&hm=bfec27079aa88932209390efac012a810f6e0b980dd614a568648c8ea03edc3d&)

When the bot is malfunctioning, you can request it to send you the training data. 

![train_data_req](https://cdn.discordapp.com/attachments/1196101538104475749/1205199490957578310/2024-02-08T2242104093159190530.png?ex=65d7807e&is=65c50b7e&hm=3775df349f7fa4d4ccf31b070725afa3b0bae0edcc3a4f672832adf88e376ac3&)

The AI model breaks and spits out the training data which will have the flag.

Flag: `actf{d3finit3ly_a_fr13nd}`
