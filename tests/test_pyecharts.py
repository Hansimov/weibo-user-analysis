from pyecharts import Bar

bar = Bar("My Fisrt Bar", "Sub Title")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.render(path="first_bar.html")