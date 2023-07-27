import importlib.util

def print_variable_value(file_path, variable_name):
    spec = importlib.util.spec_from_file_location("module_name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if hasattr(module, variable_name):
        variable_value = getattr(module, variable_name)
        print(variable_value)

if __name__ == "__main__":
    file_path = "variable_load_2.py"
    variable_name = "a"
    print_variable_value(file_path, variable_name)
