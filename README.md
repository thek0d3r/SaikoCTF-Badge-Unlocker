# SaikoCTF-Badge-Unlocker
Fully unlock the challenges for the SaikoCTF Badge given at ECSC 2024 @ Turin

---

# Dependencies
`pyserial`

---

# Run
Execute the `main.py` script to get the code running on the badge. It should generate a script called `badge.py`

The `badge.py` script contains the code that runs on the board.
Note: You might need to clean the script up.

---

# Writeup

After tinkering a bit with the badge and getting stuck on the last stage (Crypto), I decided it is time for a new approach. I starded reseaching the board a bit. It was running on a Raspberry Pi Pico W. I thought for a bit about what could be the aproaches to somehow get either access to the source code, or somehow bypass the last stage to complete the last stage.
Then I realised that it might be running micro-python. So I tried sending it a `CTRL+C` to see if I can get a <b>Micro Python Interpreter</b>.
And <i>voilla</i>, I've got a <b>Micro Python Interpreter</b> :)
From that point on, I've easily gotten access to the content of the `main.py` file that was running on the controller using this one-liner:
```py
(type("", (), {"read_main": lambda self: open("main.py").read()})()).read_main()
```
(The contents of the file can be found in `badge.py`)
Then, the flags can be found in the following `if` statements:
```py
if ch[0]== 't' and ch[1]== 'h' and ch[2]== 'e' and ch[3]== 's' and ch[4]== 'a' and ch[5]== 'i' and ch[6]== 'k' and ch[7]== 'o' and ch[8]== 'b' and ch[9]== 'a' and ch[10]== 'd' and ch[11]== 'g' and ch[12]== 'e' and ch[13]=='\\n':
```
```py
if ch[0]== 's' and ch[1]== '4' and ch[2]== '1' and ch[3]== 'k' and ch[4]== '0' and ch[5]=='\\n':
```
```py
if ch[0]== '5' and ch[1]== 'a' and ch[2]== 'i' and ch[3]== 'k' and ch[4]== 'o' and ch[5]== '4' and ch[6]== 'w' and ch[7]== 'a' and ch[8]== 'k' and ch[9]== 'e' and ch[10]== 'n' and ch[11]== 'e' and ch[12]== 'd' and ch[13]=='\\n':
```
So there you have it! The flags for the badge are:
```
"thesaikobadge"
"s14k0"
"5aiko4wakend"
```

# How can this be avoided in the future?

This kind of approach can be easily patched by just writing the logic in a function and making the code look something like this:
```py
def foo() -> bool:
    # Put the main logic here. Maybe return a status?
    return True

def main():
    try:
        if foo():
            print("Success")
        else:
            print("Failure")
    except KeyboardInterrupt:
        main()
```