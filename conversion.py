import json
import csv
import string
import random
import sys

# Initialize default elements
survey_id = "SV_" + ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(15))
trash_block_id = "BL_" + ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(15))
random_user_id = "UR_" + ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(15))
response_set_id = "RS_" + ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(15))
comma_new_line = ""

#Block variables
cur_block_index = 0
cur_block_name = ""
cur_block_id = ""
cur_flow_index = 3

#The rows of the csv componenents
question_number_index = 0
question_text_index = 2
question_type_index = 3
choices_index = 4
matrix_scale_points_index = 5
display_logic_index = 7
randomization_index = 6
block_index = 1

#Line arguments
comma_new_line_index = 3

survey_entry = {
  "SurveyID": survey_id,
  "SurveyName": "QSF Default Upload",
  "SurveyDescription": None,
  "SurveyOwnerID": random_user_id,
  "SurveyBrandID": "qxm",
  "DivisionID": None,
  "SurveyLanguage": "EN",
  "SurveyActiveResponseSet": response_set_id,
  "SurveyStatus": "Inactive",
  "SurveyStartDate": "0000-00-00 00:00:00",
  "SurveyExpirationDate": "0000-00-00 00:00:00",
  "SurveyCreationDate": "2021-06-16 11:45:33",
  "CreatorID": random_user_id,
  "LastModified": "2021-06-16 11:45:34",
  "LastAccessed": "0000-00-00 00:00:00",
  "LastActivated": "0000-00-00 00:00:00",
  "Deleted": None
}

survey_blocks = {
 "SurveyID": survey_id,
 "Element": "BL",
 "PrimaryAttribute": "Survey Blocks",
 "SecondaryAttribute": None,
 "TertiaryAttribute": None,
 "Payload": [
    {
         "Type": "Trash",
         "Description": "Trash",
         "ID": trash_block_id
    }
  ]
}

survey_flow = {
 "SurveyID": survey_id,
 "Element": "FL",
 "PrimaryAttribute": "Survey Flow",
 "SecondaryAttribute": None,
 "TertiaryAttribute": None,
 "Payload": {
    "FlowID": "FL_1",
    "Type": "Root",
    "Flow": [
      {
        "Type": "EmbeddedData",
        "FlowID": "FL_1",
        "EmbeddedData": [
          {
            "Description": "opp",
            "Type": "Custom",
            "Field": "opp",
            "VariableType": "String",
            "DataVisibility": [],
            "AnalyzeText": False,
            "Value": "QSF Default Upload"
          },
          {
            "Description": "Q_CHL",
            "Type": "Recipient",
            "Field": "Q_CHL",
            "VariableType": "String",
            "DataVisibility": [],
            "AnalyzeText": False
          },
          {
            "Description": "Q_TotalDuration",
            "Type": "Recipient",
            "Field": "Q_TotalDuration",
            "VariableType": "String",
            "DataVisibility": [],
            "AnalyzeText": False
          },
        ],
      },
      {
        "Type": "EmbeddedData",
        "FlowID": "FL_2",
        "EmbeddedData": [
          {
            "Description": "gc",
            "Type": "Custom",
            "Field": "gc",
            "VariableType": "String",
            "DataVisibility": [],
            "AnalyzeText": False,
            "Value": "1"
          }
        ]
      },
      {
        "Type": "EndSurvey",
        "FlowID": "FL_3"
      }
    ],
    "Properties": {},
  }
}

survey_options = {
 "SurveyID": survey_id,
 "Element": "SO",
 "PrimaryAttribute": "Survey Options",
 "SecondaryAttribute": None,
 "TertiaryAttribute": None,
 "Payload": {
    "BackButton": "true",
    "SaveAndContinue": "true",
    "SurveyProtection": "PublicSurvey",
    "BallotBoxStuffingPrevention": "false",
    "NoIndex": "Yes",
    "SecureResponseFiles": "true",
    "SurveyExpiration": "None",
    "SurveyTermination": "DefaultMessage",
    "Header": "",
    "Footer": "",
    "ProgressBarDisplay": "None",
    "PartialData": "+1 week",
    "ValidationMessage": "",
    "PreviousButton": " \u2190 ",
    "NextButton": " \u2192 ",
    "SurveyTitle": "QSF Default Upload",
    "SkinLibrary": "qxm",
    "SkinType": "MQ",
    "Skin": "minimal-wd1",
    "NewScoring": 1,
    "SkinLibrary": "qxm",
    "SkinType": "templated",
    "Skin": {
      "brandingId": None,
      "templateId": "*base",
      "overrides": None
    },
    "ShowExportTags": "true",
    "SurveyMetaDescription": "",
  }
}

def resetQuestionMultipleChoice():
  question_multiple_choice = {
   "SurveyID": survey_id,
   "Element": "SQ",
   "PrimaryAttribute": None,
   "SecondaryAttribute": None,
   "TertiaryAttribute": None,
   "Payload": {
      "QuestionText": None,
      "DataExportTag": None,
      "QuestionType": "MC",
      "Selector": "SAVR",
      "SubSelector": "TX",
      "Configuration": {
         "QuestionDescriptionOption": "UseText"
      },
      "QuestionDescription": None,
      "Choices": {},
      "ChoiceOrder": [],
      "Validation": {
         "Settings": {
            "ForceResponse": "ON",
            "ForceResponseType": "ON",
            "Type": "None"
         }
      },
      "Language": [],
      "NextChoiceId": 4,
      "NextAnswerId": 1,
      "QuestionID": None,
      "RecodeValues": {},
    }
  }
  return question_multiple_choice

def resetQuestionTextEntry():
  question_text_entry = {
   "SurveyID": survey_id,
   "Element": "SQ",
   "PrimaryAttribute": None,
   "SecondaryAttribute": None,
   "TertiaryAttribute": None,
   "Payload": {
      "QuestionText": None,
      "DefaultChoices": False,
      "DataExportTag": None,
      "QuestionType": "TE",
      "Selector": "SL",
      "Configuration": {
         "QuestionDescriptionOption": "UseText"
      },
      "QuestionDescription": None,
      "Validation": {
         "Settings": {
            "ForceResponse": "ON",
            "ForceResponseType": "ON",
            "Type": "None"
          }
      },
      "GradingData": [],
      "Language": [],
      "NextChoiceId": 4,
      "NextAnswerId": 1,
      "SearchSource": {
         "AllowFreeResponse": "false"
      },
      "QuestionID": None
    }
  }
  return question_text_entry

def resetRandomization():
  randomization = {
    "Type": "Advanced",
    "Advanced":
    {
      "FixedOrder":
      [],
      "RandomizeAll":
      [],
      "RandomSubSet":
      [],
      "ScaleReversal":
      [],
      "Undisplayed":
      [],
      "TotalRandSubset": 0
    },
    "ConsistentScaleReversal": False,
    "EvenPresentation": False,
    "TotalRandSubset": ""
  }
  return randomization

def resetDisplayLogic():
  display_logic = {
      "LogicType": "Question",
      "QuestionID": None,
      "QuestionIsInLoop": "no",
      "ChoiceLocator": None,
      "Operator": None,
      "QuestionIDFromLocator": None,
      "LeftOperand": None,
      "Type": "Expression",
  }

  return display_logic


def buildDefaultQsf(qsf_output, opp_name):
  qsf_output['SurveyEntry'] = survey_entry
  qsf_output['SurveyElements'] = []
  qsf_output['SurveyElements'].append(survey_blocks)
  qsf_output['SurveyElements'].append(survey_flow)
  qsf_output['SurveyElements'].append(survey_options)
  if opp_name != "":
    print(opp_name)
    qsf_output['SurveyElements'][1]["Payload"]["Flow"][0]["EmbeddedData"][0]["Value"] = opp_name
  return qsf_output

def gatherCsvData(qsf_input, csv_input_name):
  global comma_new_line
  if 0 <= comma_new_line_index < len(sys.argv):
    comma_new_line = "comma"
  else:
    comma_new_line = "new line"

  try:
    if ".csv" not in csv_input_name:
      csv_input_name = csv_input_name + ".csv"

    with open(csv_input_name) as csvfile:
      qsf_input = []
      reader = csv.reader(csvfile)
      for row in reader:
          qsf_input.append(row)
  except IOError:
    print("There is no csv file with that name. Try again with a different file name. \n")
    sys.exit()
  if not qsf_input:
    input("There is no data in that file. Try again with a different file. \n")
    sys.exit()
  return qsf_input

def buildTextQuestionType(question, cur_question):
  if question[question_type_index].lower() == "text":
    cur_question["Payload"]["QuestionType"] = "DB"
    cur_question["Payload"]["Selector"] = "TB"
    cur_question["Payload"]["Randomization"] = None
    cur_question["Payload"]["Validation"]["Settings"] = {"Type": "None"}
    cur_question["Payload"]["DefaultChoices"] = False
    del cur_question["Payload"]["SubSelector"]
    del cur_question["Payload"]["Choices"]
    del cur_question["Payload"]["RecodeValues"]
    del cur_question["Payload"]["Randomization"]
  return cur_question

def buildMatrixTableQuestionType(question, cur_question):
  if "matrix table" in question[question_type_index].lower():
    cur_question["Payload"]["QuestionType"] = "Matrix"
    cur_question["Payload"]["Selector"] = "Likert"
    if "multiple" in question[question_type_index].lower():
      cur_question["Payload"]["SubSelector"] = "MultipleAnswer"
    else:
      cur_question["Payload"]["SubSelector"] = "SingleAnswer"

    cur_question["Payload"]["Configuration"] = {
    "QuestionDescriptionOption": "UseText",
    "TextPosition": "inline",
    "ChoiceColumnWidth": 25,
    "RepeatHeaders": "none",
    "WhiteSpace": "OFF",
    "MobileFirst": True
    }
    cur_question["Payload"]["Answers"] = {}
    cur_question["Payload"]["AnswerOrder"] = []
    cur_question["Payload"]["DefaultChoices"] = False
    cur_question["Payload"]["NextAnswerId"] = 4
  return cur_question

def buildChoices(question, cur_question):
  if "matrix table" in question[question_type_index].lower() or "multiple choice" in question[question_type_index].lower():
    if comma_new_line == "comma":
      choices = question[choices_index].split(",")
    else:
      choices = question[choices_index].split("\n")

    for choice_iteration, choice in enumerate(choices):
      bad_input_offset = 0
      exclusive_option = "exclusive"
      text_entry_option = "text entry"
      anchor_option = "anchor"
      cur_choice = {"Display":choice.strip()}

      if choice.strip() == "":
        #This is meant to offset the choice iteration if there is bad input
        #Should be very rare so not persuing
        bad_input_offset = bad_input_offset + 1
        continue

      #Get exclusive options
      if exclusive_option in choice.lower():
        cur_choice["Display"] = choice.split("[", 1)[0].strip()
        cur_choice["ExclusiveAnswer"] = True

      #Get text entry options
      if text_entry_option in choice.lower():
        cur_choice["Display"] = choice.split("[", 1)[0].strip()
        cur_choice["TextEntry"] = "true"
        cur_choice["TextEntryForceResponse"] = True

      #Get anchor options
      if "Randomization" in cur_question["Payload"]:
        if anchor_option in choice.lower():
          if cur_question["Payload"]["Randomization"]["Type"] != "Advanced":
            #Change randomization to advanced
            FixedOrder = []
            RandomizeAll = []
            randomization = resetRandomization()
            for random_order_choice in range(choice_iteration):
              FixedOrder.append("{~Randomized~}")
              RandomizeAll.append(str(random_order_choice + 1))

            FixedOrder.append(str(choice_iteration + 1))
            randomization["Advanced"]["FixedOrder"] = FixedOrder
            randomization["Advanced"]["RandomizeAll"] = RandomizeAll
            cur_question["Payload"]["Randomization"] = randomization
          else:
            #Add choice to advanced randomization list
            FixedOrder.append(str(choice_iteration + 1))
        elif cur_question["Payload"]["Randomization"]["Type"] == "Advanced": 
          #Add a non-anchor choice to advanced randomization
          FixedOrder.append("{~Randomized~}")
          RandomizeAll.append(str(random_order_choice + 1))

      cur_question["Payload"]["Choices"][choice_iteration + 1] = cur_choice
      cur_question["Payload"]["ChoiceOrder"].append(str(choice_iteration + 1))
  return cur_question

def buildMatrixTableScalePoints(question, cur_question):
  if "matrix table" in question[question_type_index].lower():
    if comma_new_line == "comma":
      scale_points = question[matrix_scale_points_index].split(",")
    else:
      scale_points = question[matrix_scale_points_index].split("\n")

    for scale_iteration, scale_point in enumerate(scale_points):
      cur_scale_point = {
        "Display":scale_point.strip()
      }

      if scale_point.strip() == "":
        continue

      cur_question["Payload"]["Answers"][scale_iteration + 1] = cur_scale_point
      cur_question["Payload"]["AnswerOrder"].append(str(scale_iteration + 1))
  return cur_question

def addBlockToFlow(qsf_output):
  global cur_flow_index
  cur_flow_index = cur_flow_index + 1
  cur_flow_id = "FL_" + str(cur_flow_index)

  cur_flow_element = {
    "ID":cur_block_id,
    "Type":"Block",
    "FlowID":cur_flow_id
  }
  qsf_output['SurveyElements'][1]["Payload"]["Flow"].insert(-2,cur_flow_element)
  flow_count = {
    "Count":cur_flow_index
  }
  qsf_output['SurveyElements'][1]["Payload"]["Properties"] = flow_count
  return qsf_output

def addQuestionToBlock(question_iteration, qsf_output, question, qsf_input):
  global cur_block_index
  global cur_block_name
  global cur_block_id

  if cur_block_index == 0:
    #create the first block
    default_block_id = "BL_" + ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(15))
    default_block = {
     "Type": "Default",
     "Description": question[block_index],
     "ID": default_block_id,
     "BlockElements": []
    }
    qsf_output['SurveyElements'][0]["Payload"].append(default_block)
    cur_block_index = cur_block_index + 1
    cur_block_name = question[block_index]
    cur_block_id = default_block_id
    addBlockToFlow(qsf_output)

  if cur_block_name != question[block_index] and question[block_index] != "":
    #delete the previous page break
    del qsf_output['SurveyElements'][0]["Payload"][cur_block_index]["BlockElements"][-1]

    #create a new block
    next_block_id = "BL_" + ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(15))
    next_block = {
     "Type": "Standard",
     "Description": question[block_index],
     "ID": next_block_id,
     "BlockElements": []
    }
    qsf_output['SurveyElements'][0]["Payload"].append(next_block)
    cur_block_index = cur_block_index + 1
    cur_block_name = question[block_index]
    cur_block_id = next_block_id
    addBlockToFlow(qsf_output)

  #add the current question to the block
  cur_block_element = {
    "Type":"Question",
    "QuestionID":"QID" + str(question_iteration + 1)
  }
  qsf_output['SurveyElements'][0]["Payload"][cur_block_index]["BlockElements"].append(cur_block_element)

  #Add page break between questions
  if question_iteration != len(qsf_input) - 2:
    qsf_output['SurveyElements'][0]["Payload"][cur_block_index]["BlockElements"].append({"Type": "Page Break"})
  return qsf_output

def buildDisplayLogic(question, cur_question, qsf_output):
  if question[display_logic_index] == "":
    return cur_question

  display_logic_value = {
    "0": {}
  }
  
  if comma_new_line == "comma":
    display_logics = question[display_logic_index].split(",")
  else:
    display_logics = question[display_logic_index].split("\n")

  for display_logic_iteration, display_logic in enumerate(display_logics):
    cur_display_logic = resetDisplayLogic()

    cur_export_tag = display_logics[display_logic_iteration].split("is",1)[0].strip()
    if display_logic_iteration > 0:
      conjunction = cur_export_tag.split()[0]
      cur_export_tag = cur_export_tag.split(' ', 1)[1]
      cur_display_logic["Conjuction"] = conjunction.capitalize()

    cur_choice_index = display_logics[display_logic_iteration].split()[-1].strip()
    if "is not" in display_logics[display_logic_iteration]:
      Operator = "NotSelected"
    else:
      Operator = "Selected"

    cur_display_logic["Operator"] = Operator

    for question_iteration, question in enumerate(qsf_output["SurveyElements"]):
      if "DataExportTag" in question["Payload"] and question["Payload"]["DataExportTag"] == cur_export_tag:
        QuestionID = question["PrimaryAttribute"]
        ChoiceLocator = "q://" + QuestionID + "/SelectableChoice/" + cur_choice_index
        continue

    cur_display_logic["QuestionID"] = QuestionID
    cur_display_logic["ChoiceLocator"] = ChoiceLocator
    cur_display_logic["QuestionIDFromLocator"] = QuestionID
    cur_display_logic["LeftOperand"] = ChoiceLocator
    display_logic_value["0"][str(display_logic_iteration)] = cur_display_logic

  display_logic_value["0"]["Type"] = "If"
  display_logic_value["Type"] = "BooleanExpression"
  display_logic_value["inPage"] = False
  cur_question["Payload"]["DisplayLogic"] = display_logic_value
  return cur_question

def createQuestions(qsf_input, qsf_output):
  for question_iteration, question in enumerate(qsf_input[1:]):
    if question[question_type_index].lower() != "text entry":
      cur_question = resetQuestionMultipleChoice()
    else:
      cur_question = resetQuestionTextEntry()

    cur_question["PrimaryAttribute"] = "QID" + str(question_iteration + 1)
    cur_question["SecondaryAttribute"] = question[question_text_index]
    cur_question["Payload"]["QuestionText"] = question[question_text_index]
    cur_question["Payload"]["DataExportTag"] = str(question[question_number_index])
    cur_question["Payload"]["QuestionDescription"] = question[question_text_index]
    cur_question["Payload"]["QuestionID"] = "QID" + str(question_iteration + 1)

    #Update to multiple select question type
    if "multiple select" in question[question_type_index].lower():
      cur_question["Payload"]["Selector"] = "MAVR"

    #Add randomization
    if question[randomization_index].lower() == "yes":
      cur_question["Payload"]["Randomization"] = {
        "Advanced": None,
        "Type": "All",
        "TotalRandSubset": ""
      }

    #Update to text question type
    cur_question = buildTextQuestionType(question, cur_question)

    #Update to matrix table question type
    cur_question = buildMatrixTableQuestionType(question, cur_question)
    
    # Get choices for multiple choice questions
    cur_question = buildChoices(question, cur_question)

    #Get matrix table scale points
    cur_question = buildMatrixTableScalePoints(question, cur_question)

    #Build display logic
    cur_question = buildDisplayLogic(question, cur_question, qsf_output)

    qsf_output['SurveyElements'].append(cur_question)

    # Add question to block
    qsf_output = addQuestionToBlock(question_iteration, qsf_output, question, qsf_input)
  return qsf_output

def convertCsvToQsf(qsf_output):
  with open('output.qsf', 'w') as outfile:
      json.dump(qsf_output, outfile)