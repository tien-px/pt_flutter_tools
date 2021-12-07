//ignore_for_file: close_sinks
import 'package:pt_flutter_architecture/pt_flutter_architecture.dart';
import 'package:get/get.dart' as GetX;
import 'package:{{ package_name }}/scenes/{{ name_lower }}/{{ name_lower }}_navigator.dart';
import 'package:{{ package_name }}/scenes/{{ name_lower }}/{{ name_lower }}_usecase.dart';
import 'package:rxdart/rxdart.dart';

class {{ name }}VMI {
  var onLoad = subject<void>();
}

class {{ name }}VMO {
  
}

class {{ name }}ViewModel
    extends RxViewModel<{{ name }}VMI, {{ name }}VMO> {
  {{ name }}NavigatorType navigator;
  {{ name }}SceneUseCaseType useCase;

  {{ name }}ViewModel({required this.navigator, required this.useCase});

  @override
  {{ name }}VMO transform({{ name }}VMI input) {
    super.transform(input);
    var output = {{ name }}VMO();

    input.onLoad.subscribe().disposedBy(bag);

    return output;
  }
}
