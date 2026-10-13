import script1
x = 4
def something():
    import script1
    if __name__ == "__main__":
        print(x)
    elif __name__ == "script1":
        print(script1.x)
something()