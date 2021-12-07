// DO NOT EDIT. This is code generated via ptflutter

const _assetsImagePath = '{{ image_folder }}';

class Images {
  {% for file in files %}
  static const {{ file.image_name }} = '$_assetsImagePath/{{ file.image_file }}';
  {% endfor %}
}
