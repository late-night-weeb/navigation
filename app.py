from flask import Flask, render_template, request, redirect, url_for, jsonify
from urllib.parse import unquote
import json
import os
import uuid

app = Flask(__name__)

DATA_FILE = 'data.json'
CATEGORY_FILE = 'category.json'
COLOR_FILE = 'colors.json'




def load_data(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            return json.load(f)
    return []

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def normalize_tile(tile):
    keys = ["id", "name", "website", "port", "username", "password", "email", "protocol", "image", "category", "color"]
    return {k: tile.get(k) or "" for k in keys}

@app.route('/')
def index():
    tiles = load_data(DATA_FILE)
    categories = load_data(CATEGORY_FILE)
    colors = load_data(COLOR_FILE)
    categorized_tiles = {cat: [] for cat in categories}
    for tile in tiles:
        norm_tile = normalize_tile(tile)
        categorized_tiles.setdefault(norm_tile.get('category', 'Uncategorized'), []).append(norm_tile)
    return render_template('index.html', tiles=categorized_tiles, categories=categories, colors=colors)


@app.route('/add_tile', methods=['POST'])
def add_tile():
    tiles = load_data(DATA_FILE)
    new_tile = request.form.to_dict()
    new_tile['id'] = str(uuid.uuid4())  # <-- Unique ID here
    tiles.append(new_tile)
    save_data(DATA_FILE, tiles)
    return redirect(url_for('index'))


@app.route('/delete_tile/<tile_id>', methods=['POST'])
def delete_tile(tile_id):
    tiles = load_data(DATA_FILE)
    tiles = [tile for tile in tiles if tile['id'] != tile_id]
    save_data(DATA_FILE, tiles)
    return redirect(url_for('index'))


@app.route('/add_category', methods=['POST'])
def add_category():
    categories = load_data(CATEGORY_FILE)
    new_cat = request.form['new_category']
    if new_cat and new_cat not in categories:
        categories.append(new_cat)
        save_data(CATEGORY_FILE, categories)
    return redirect(url_for('index'))

@app.route('/delete_category/<category>', methods=['POST'])
def delete_category(category):
    categories = load_data(CATEGORY_FILE)
    categories = [c for c in categories if c != category]
    save_data(CATEGORY_FILE, categories)
    return redirect(url_for('index'))

@app.route("/add_color", methods=["POST"])
def add_color():
    colors = load_data(COLOR_FILE)
    color_name = request.form.get("color_name")
    color_value = request.form.get("new_color")
    if color_name and color_value:
        if color_name not in colors:
            colors[color_name] = color_value
            save_data(COLOR_FILE, colors)
    return redirect(url_for("index"))



@app.route("/delete_color/<path:color>", methods=["POST"])
def delete_color(color):
    color = unquote(color)
    colors = load_data(COLOR_FILE)
    if color in colors:
        colors.remove(color)
        save_data(COLOR_FILE, colors)
    return redirect(url_for("index"))



@app.route("/edit_tile/<tile_id>", methods=["POST"])
def edit_tile(tile_id):
    data = load_data(DATA_FILE)
    for tile in data:
        if tile["id"] == tile_id:
            tile["name"] = request.form.get("name")
            tile["website"] = request.form.get("website")
            tile["port"] = request.form.get("port")
            tile["username"] = request.form.get("username")
            tile["password"] = request.form.get("password")
            tile["email"] = request.form.get("email")
            tile["protocol"] = request.form.get("protocol")
            tile["image"] = request.form.get("image")
            tile["category"] = request.form.get("category")
            tile["color"] = request.form.get("color")
            break
    save_data(DATA_FILE, data)
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
