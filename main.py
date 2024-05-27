from flask import Flask, render_template, request
import time
import src.ai.nums as nums
import src.ai.img as img
import sys
import os


loaded = {
    "numbers": False,
    "images": False,
    "text": False    
}

app = Flask(__name__, static_folder='src/web/static', template_folder='src/web/templates')




@app.route("/")
def home():
    return render_template("index.html")


@app.route("/numbers", methods=["POST", "GET"])
def numbers():
    if loaded["numbers"] and request.method == "POST":
        inp = request.form["number"]
        output = nums.get(inp)
        out = ""
        for number in output:
            out += str(round(float(number[0]), 2)) + " "
        return render_template("model/numbers.html", input=inp, guess=out)

    
    else:
        if request.method == "GET":
            loaded["numbers"] = False
            return render_template("loader/numbers.html", error="")
            


        elif request.method == "POST":
            status = ""
            epochs = request.form["epochs"]
            sq1 = request.form["sq1"]
            sq2 = request.form["sq2"]

        
            try:
                int(epochs)
            except ValueError:
                
                loaded["numbers"] = False
                status += "Invalid Epochs"
            
            if len(sq1.split(" ")) != len(sq2.split(" ")) or len(sq1) == 0:
                status += "\nInvalid Sequences"

            
            print(f"Status:     {'Success' if status == '' else 'Failed'}\nEpochs:    {epochs}\nSequence 1:   {sq1}\nSequence 2:   {sq2}\nError: {status if status != '' else 'None'}")
            
            if status == "":
                render_template("model/numbers.html")
                loaded["numbers"] = True
                nums.load(int(epochs), sq1, sq2)
                time.sleep(3)
                print("Model loaded")
                return render_template("model/numbers.html")
            else:
                return render_template("loader/numbers.html", error=status) 
    return render_template("loader/numbers.html", error="")
            

@app.route("/images", methods=["POST", "GET"])
def images():
    if request.method == "POST" and loaded["images"]:
        inp = request.form["data"]
        with open("store.txt", "w") as f:
            f.write(inp)
        output = img.get(inp)
        return render_template("model/images.html", guess=output)
    
    else:
        if request.method == "GET":
            loaded["images"] = False
            return render_template("loader/images.html", error="")
            


        elif request.method == "POST":
            status = ""
            epochs = request.form["epochs"]
        
            try:
                int(epochs)
            except ValueError:
                
                loaded["images"] = False
                status = "Invalid Epochs"

            
            print(f"Status:     {'Success' if status == '' else 'Failed'}\nEpochs:    {epochs}\nError: {status if status != '' else 'None'}")
            
            time.sleep(1)
            if status == "":
                img.load(int(epochs))
                loaded["images"] = True
                time.sleep(3)
                print("Redirecting...")
                return render_template("model/images.html")
            else:
                return render_template("loader/numbers.html", error=status) 
    return render_template("loader/images.html", error="")
            





if __name__ == "__main__":
    if sys.argv[-1] == "debug":
        import src.ai.img as img

        with open("store.txt", "r") as f:
            data = f.read().split(",")

        print(data)
        img.showBigArr(data)
        newdata = img.compress(data)
        img.showArr(newdata)
    else:
       app.run(debug=True)