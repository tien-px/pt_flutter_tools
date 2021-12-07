// DO NOT EDIT. This is code generated via ptflutter

import 'package:pt_flutter_architecture/pt_flutter_architecture.dart';
{% for file in import_files %}
import '{{ file }}';
{% endfor %}

class RxDebug {
  static bool isEnabled = false;
  {% for item in items %}

  static void {{ item.method_name }}(
      List<Stream> input, {{ item.output_class_name }}VMO output, DisposeBag bag) {
    if (!isEnabled) return;
    
    {% for input in item.inputs %}
    input[{{ loop.index0 }}].cast().debug("{{ input }}").subscribe().disposedBy(bag);
    {% endfor %}

    {% for output in item.outputs %}
    output.{{ output }}.stream
        .debug("{{ output }}")
        .subscribe()
        .disposedBy(bag);
    {% endfor %}
  }
  {% endfor %}
}
