import 'package:pt_flutter_architecture/pt_flutter_architecture.dart';
import 'package:{{ package_name }}/assembler.dart';
{% if include_mock %}
import 'package:{{ package_name }}/mock/{{ name_lower }}_usecase_mock.dart';
{% endif %}

import '{{ name_lower }}_navigator.dart';
import '{{ name_lower }}_usecase.dart';
import '{{ name_lower }}_view.dart';
import '{{ name_lower }}_viewmodel.dart';

extension {{ name }}Assembler on Assembler {
  {% if include_mock %}
  static const isMock = bool.fromEnvironment("mock");
  
  {% endif %}
  {{ name }}View resolve{{ name }}View() {
    return {{ name }}View(viewModel: _resolve{{ name }}ViewModel());
  }

  {{ name }}ViewModel _resolve{{ name }}ViewModel() {
    return {{ name }}ViewModel(
        navigator: _resolve{{ name }}Navigator(),
        useCase: _resolve{{ name }}SceneUseCase());
  }

  {{ name }}NavigatorType _resolve{{ name }}Navigator() {
    return {{ name }}Navigator(assembler: this);
  }

  {{ name }}SceneUseCaseType _resolve{{ name }}SceneUseCase() {
    return {{ name }}SceneUseCase();
    {% if include_mock %}
    return  isMock ? {{ name }}SceneUseCaseMock() : {{ name }}SceneUseCase();
    {% else %}
    return {{ name }}SceneUseCase();          
    {% endif %}
  }
}
