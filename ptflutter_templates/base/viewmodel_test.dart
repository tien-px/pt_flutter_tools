import 'package:{{ package_name }}/scenes/{{ name_lower }}/{{ name_lower }}_viewmodel.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:pt_flutter_architecture/pt_flutter_architecture.dart';
import 'package:rxdart/rxdart.dart';

import '{{ name_lower }}_navigator_mock.dart';
import '{{ name_lower }}_usecase_mock.dart';

void main() {
  var loadTrigger = PublishSubject<void>();

  {{ name }}NavigatorMock navigator;
  {{ name }}SceneUseCaseMock useCase;
  {{ name }}ViewModel viewModel;
  DisposeBag bag;

  setUp(() {
    navigator = {{ name }}NavigatorMock();
    useCase = {{ name }}SceneUseCaseMock();
    viewModel = {{ name }}ViewModel(navigator: navigator, useCase: useCase);
    bag = DisposeBag();
    var input = {{ name }}VMI(loadTrigger: loadTrigger);
    var output = viewModel.transform(input, bag);
    output.loaded.listen(null).disposedBy(bag);
  });

  tearDown(() async {
    await bag.dispose();
  });

  emit(Subject subject) async {
    subject.add(null);
    await Future.delayed(Duration(milliseconds: 100));
  }

  group('{{ name_lower }}_test', () {
    test('something', () async {
      // Arrange
      // Act
      await emit(loadTrigger);
      // Assert
      expect(true, true);
    });
  });
}
