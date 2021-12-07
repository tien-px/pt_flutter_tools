import 'package:pt_flutter_architecture/pt_flutter_architecture.dart';
import 'package:flutter/material.dart';
import 'package:{{ package_name }}/scenes/base/base.dart';
import 'package:{{ package_name }}/scenes/{{ name_lower }}/{{ name_lower }}_viewmodel.dart';

class {{ name }}View extends RxView<{{ name }}ViewModel> {
  late final {{ name }}VMI input;
  late final {{ name }}VMO output;

  @override
  void bindViewModel() {
    input = {{ name }}VMI();
    output = viewModel.transform(input);
    input.onLoad.emit();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(),
    );
  }
}
