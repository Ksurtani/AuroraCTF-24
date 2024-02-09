
# Friend or foe?

A brief solution of how to solve this challenge which was given in ISTE and MIST Aurora CTF.


## Solution

This challenge is based off a new injection techniques, i.e, prompt injections. The player is given access to a discord server which has a bot with the name `sudo.Aura`. This bot has the uses an open source Llama AI model, `dolphin-2.0-mistral-7B-GGUF`.

The Llama AI models can be manipulated using the ethical reasoning methods like `do <a task> to save <something>`. You will know that the injection is working when you get same replies repeatedly.

![breakdown](https://raw.githubusercontent.com/ManipalInformationSecurityTeam/AuroraCTF-24/main/Friend%20Or%20Foe%3F/chat1.png)

When the bot is malfunctioning, you can request it to send you the training data. 

![train_data_req](https://raw.githubusercontent.com/ManipalInformationSecurityTeam/AuroraCTF-24/main/Friend%20Or%20Foe%3F/chat2.png)

The AI model breaks and spits out the training data which will have the flag.

Flag: `actf{d3finit3ly_a_fr13nd}`
