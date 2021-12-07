// DO NOT EDIT. This is code generated via ptflutter
// ignore_for_file: non_constant_identifier_names, camel_case_types

import 'package:easy_localization/easy_localization.dart';

class i18n {
  {% for item in items %}
  static String get {{ item.name }} => '{{ item.key }}'.tr();
  {% endfor %}
}
