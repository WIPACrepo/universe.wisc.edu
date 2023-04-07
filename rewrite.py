import os

for root,dirs,files in os.walk('.'):
    for f in files:
        if not f.endswith('.html'):
            continue
        path = os.path.join(root,f)
        with open(path) as f:
            data = f.read()
        data = data.replace("href='http://universe.wisc.edu/", "href='/")
        data = data.replace('href="http://universe.wisc.edu/', 'href="/')
        data = data.replace('href="http://universe.wisc.edu/', 'href="/')
        data = data.replace("src='http://universe.wisc.edu/", "src='/")
        data = data.replace('src="http://universe.wisc.edu/', 'src="/')
        data = data.replace('http://universe.wisc.edu/wp-content', '/wp-content')

        data = data.replace("http://universe.wisc.edu", "https://universe.wisc.edu")
        
        with open(path,'w') as f:
            f.write(data)

