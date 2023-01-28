from flask import Flask, render_template, request, redirect, jsonify
import youtube_dl
app = Flask(__name__)


@app.route('/', methods=['GET'])
def display_url():
	url = request.args.get('url')
	with youtube_dl.YoutubeDL() as ydl:
		url = ydl.extract_info(url, download=False)
		print(url)
		try:
			download_link = url["entries"][-1]["formats"][-1]["url"]
		except:
			download_link = url["formats"][-1]["url"]
		#return redirect(download_link+"&dl=1")
		return jsonify(download_link=download_link)
		#return jsonify(download_link)

if __name__ == '__main__':
	app.run(debug=False,host='0.0.0.0')
