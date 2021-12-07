@override
String toString() {
  return """{{ name }}{
    {% for p in properties %}
    {{ p.name }}: ${{ p.name }}{{ "," if not loop.last }}
    {% endfor %}}""";
}