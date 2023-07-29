#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        gravity = float(request.form.get("gravity"))
        ph = float(request.form.get("ph"))
        osmo = float(request.form.get("osmo"))
        cond = float(request.form.get("cond"))
        urea = float(request.form.get("urea"))
        calc = float(request.form.get("calc"))
        return(render_template("index.html", result=-0.04191465 + (gravity * -3.94579654e-02) + (ph * -3.94579654e-02) + (osmo * 3.05883681e-04) + (cond * -8.53476004e-02) + (urea * 1.12604054e-03) + (calc * 7.20512124e-01)))
    else:
        return(render_template("index.html", result="waiting"))

if __name__ == "__main__" :
    app.run()



# In[ ]:




