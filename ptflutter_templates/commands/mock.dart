{% if is_abstract %}
class {{ class_name }}Mock implements {{ abstract_name }} {
{% endif %}
    {% for f in functions %}
    /// {{ f.overloaded_name }}

    var {{ f.overloaded_name }}_Called = false;
    {% if not f.return_void %}
    {% if f.return_nil %}
    var {{ f.overloaded_name }}_ReturnValue: {{ f.return_type }} = {{ f.return_value }};
    {% else %}
    var {{ f.overloaded_name }}_ReturnValue = {{ f.return_value }};
    {% endif %}
    {% endif %}

    {{ f.origin }} {
        {{ f.overloaded_name }}_Called = true;
    {% if not f.return_void %}
        return {{ f.overloaded_name }}_ReturnValue;
    {% endif %}
    } {{ '\n' if not loop.last }}
    {% endfor %}
{{ '}' if is_abstract }}