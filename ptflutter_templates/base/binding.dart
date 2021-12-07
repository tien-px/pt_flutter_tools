import 'package:pt_flutter_architecture/pt_flutter_architecture.dart';
import 'package:{{ package_name }}/scenes/{{ name_lower }}/{{ name_lower }}_navigator.dart';
import 'package:{{ package_name }}/scenes/{{ name_lower }}/{{ name_lower }}_usecase.dart';
import 'package:{{ package_name }}/mock/{{ name_lower }}_usecase_mock.dart';
import 'package:{{ package_name }}/scenes/{{ name_lower }}/{{ name_lower }}_viewmodel.dart';

class  {{ name }}Binding implements Bindings {
  {% if include_mock %}
  static const isMock = bool.fromEnvironment("mock");
  {% endif %}
  @override
  void dependencies() {
    Get.lazyPut< {{ name }}ViewModel>(() {
      return  {{ name }}ViewModel(
          navigator:  {{ name }}Navigator(),
          {% if include_mock %}
          useCase:  isMock ? {{ name }}SceneUseCaseMock() : {{ name }}SceneUseCase());
          {% else %}
          useCase:  {{ name }}SceneUseCase());          
          {% endif %}
    });
  }
}
