// DO NOT EDIT. This is code generated via ptflutter

import 'package:pt_flutter_object_mapper/pt_flutter_object_mapper.dart';
{% for file in import_files %}
import '{{ file }}';
{% endfor %}

class Entities {
  static void register() {
    {% for class in classes %}
    Mappable.factories[{{ class }}] = () => {{ class }}();
    {% endfor %}
  }
}

