import json

with open("./resources/json/utils.json") as json_file:
    input_helper = json.load(json_file)
    help_details = input_helper.get('help')
    case_details = input_helper.get('case')
    problem_details = input_helper.get("problem")
    satisfaction_details = input_helper.get('satisfaction')

