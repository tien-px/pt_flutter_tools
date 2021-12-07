/// Remember register to Mappable.factories
/// Mappable.factories[{{ name }}] = () => {{ name }}();

class {{ name }} with Mappable {
  {% for p in properties %}
  {{ p.type_name }} {{ p.name }};
  {% endfor %}

  @override
  void mapping(Mapper map) {
    {% for p in properties %}
    {% if p.is_date %}
    map("{{ p.raw_name }}", {{ p.name }}, (v) => {{ p.name }} = v, DateTransform());
    {% elif p.is_dart_type %}
    map("{{ p.raw_name }}", {{ p.name }}, (v) => {{ p.name }} = v);
    {% else %}
    map<{{ p.type_name.replace('List<','').replace('>','') }}>("{{ p.raw_name }}", {{ p.name }}, (v) => {{ p.name }} = v);
    {% endif %}
    {% endfor %}
  }
}
