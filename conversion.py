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
scoring_id = "SC_" + ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(15))
preview_term_id = "BL_" + ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(15))
preview_variables_id = "BL_" + ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(15))
comma_new_line = ""

#Block variables
cur_block_index = 0
cur_block_name = ""
cur_block_id = ""
cur_flow_index = 3
skip_logic_id = 1
final_question_id = 0

#The rows of the csv componenents
question_number_index = 0
question_text_index = 2
question_type_index = 3
choices_index = 4
matrix_scale_points_index = 5
display_logic_index = 7
randomization_index = 6
block_index = 1
term_index = 8

#Line arguments
comma_new_line_index = 3

survey_entry = {
  "SurveyID": survey_id,
  "SurveyName": "Qualtrics Survey | Qualtrics Experience Management",
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
    "SurveyTitle": "Qualtrics Survey | Qualtrics Experience Management",
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

scoring = {
  "SurveyID": survey_id,
  "Element": "SCO",
  "PrimaryAttribute": "Scoring",
  "SecondaryAttribute": None,
  "TertiaryAttribute": None,
  "Payload":
  {
      "ScoringCategories":
      [
          {
              "ID": scoring_id,
              "Name": "Score",
              "Description": ""
          }
      ],
      "ScoringCategoryGroups":
      [],
      "DefaultScoringCategory": scoring_id,
      "ScoringSummaryCategory": None,
      "ScoringSummaryAfterQuestions": 0,
      "ScoringSummaryAfterSurvey": 0,
      "AutoScoringCategory": None
  }
}

preview_term_question = {
  "SurveyID": survey_id,
  "Element": "SQ",
  "PrimaryAttribute": None,
  "SecondaryAttribute": "Only shown in preview   term: ${e://Field/term} gc: ${e://Field/gc}",
  "TertiaryAttribute": None,
  "Payload":
  {
    "QuestionText": "<strong><span style=\"color:#e74c3c;\">Only shown in preview</span></strong>\n<div>&nbsp;</div>\n\n<div>term:&nbsp;${e://Field/term}</div>\n\n<div>gc:&nbsp;${e://Field/gc}</div>",
    "DefaultChoices": False,
    "DataExportTag": "Preivew: Term",
    "QuestionID": None,
    "QuestionType": "DB",
    "Selector": "TB",
    "Configuration":
    {
        "QuestionDescriptionOption": "UseText"
    },
    "QuestionDescription": "Only shown in preview   term: ${e://Field/term} gc: ${e://Field/gc}",
    "ChoiceOrder":
    [],
    "Validation":
    {
      "Settings":
      {
          "Type": "None"
      }
    },
    "GradingData":
    [],
    "Language":
    [],
    "NextChoiceId": 4,
    "NextAnswerId": 1
  }
}

preview_variables_question = {
  "SurveyID": survey_id,
  "Element": "SQ",
  "PrimaryAttribute": None,
  "SecondaryAttribute": "Only shown in preview   Variable Name: ",
  "TertiaryAttribute": None,
  "Payload":
  {
    "QuestionText": "<strong><span style=\"color:#e74c3c;\">Only shown in preview</span></strong>\n<div>&nbsp;</div>\n\n<div>Variable Name:&nbsp;</div>",
    "DefaultChoices": False,
    "DataExportTag": "Preview: Variables",
    "QuestionID": None,
    "QuestionType": "DB",
    "Selector": "TB",
    "Configuration":
    {
        "QuestionDescriptionOption": "UseText"
    },
    "QuestionDescription": "Only shown in preview   Variable Name: ",
    "ChoiceOrder":
    [],
    "Validation":
    {
      "Settings":
      {
          "Type": "None"
      }
    },
    "GradingData":
    [],
    "Language":
    [],
    "NextChoiceId": 4,
    "NextAnswerId": 1
  }
}

def resetPreviewBlock():
  preview_block = {
    "Type": "Standard",
    "SubType": "",
    "Description": None,
    "ID": None,
    "BlockElements":
    [
      {
        "Type": "Question",
        "QuestionID": None
      }
    ]
  }
  return preview_block

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

def resetSkipLogic():
  skip_logic = {
    "ChoiceLocator": None,
    "Condition": None,
    "Locator": None,
    "QuestionID": None,
    "SkipLogicID": 0,
    "SkipToDestination": None,
  }
  return skip_logic


def buildDefaultQsf(qsf_output, opp_name):
  qsf_output['SurveyEntry'] = survey_entry
  qsf_output['SurveyElements'] = []
  qsf_output['SurveyElements'].append(survey_blocks)
  qsf_output['SurveyElements'].append(survey_flow)
  qsf_output['SurveyElements'].append(survey_options)
  qsf_output['SurveyElements'].append(scoring)
  if opp_name != "":
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
      choices = question[choices_index].split(";")
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
          cur_choice["Display"] = choice.split("[", 1)[0].strip()
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
      scale_points = question[matrix_scale_points_index].split(";")
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

def buildSkipLogic(question, cur_question, qsf_output):
  if question[term_index] == "":
    return cur_question

  if comma_new_line == "comma":
    skip_logics = question[term_index].split(";")
  else:
    skip_logics = question[term_index].split("\n")

  skip_logic_value = []

  for skip_logic_iteration, skip_logic in enumerate(skip_logics):
    cur_skip_logic = resetSkipLogic()

    cur_choice_index = skip_logics[skip_logic_iteration].split()[-1].strip()
    if "is not" in skip_logics[skip_logic_iteration].lower():
      Condition = "NotSelected"
    else:
      Condition = "Selected"

    cur_skip_logic["Condition"] = Condition
    cur_skip_logic["QuestionID"] = cur_question["PrimaryAttribute"]
    cur_skip_logic["ChoiceLocator"] = "q://" + str(cur_question["PrimaryAttribute"]) + "/SelectableChoice/" + str(cur_choice_index)
    cur_skip_logic["Locator"] = "q://" + str(cur_question["PrimaryAttribute"]) + "/SelectableChoice/" + str(cur_choice_index)
    cur_skip_logic["SkipToDestination"] = "ENDOFBLOCK"

    global skip_logic_id
    cur_skip_logic["SkipLogicID"] = skip_logic_id
    skip_logic_id = skip_logic_id + 1

    skip_logic_value.append(cur_skip_logic)

  qsf_output["SurveyElements"][0]["Payload"][cur_block_index]["BlockElements"][-2]["SkipLogic"] = skip_logic_value
  return cur_question

def buildTerms(question, cur_question, qsf_output):
  if question[term_index] == "":
    return cur_question

  global cur_flow_index
  cur_flow_index = cur_flow_index + 1
  branch_flow_id = "FL_" + str(cur_flow_index)
  cur_flow_index = cur_flow_index + 1
  data_flow_id = "FL_" + str(cur_flow_index)
  cur_flow_index = cur_flow_index + 1
  term_flow_id = "FL_" + str(cur_flow_index)

  cur_term_block = {
    "Type": "Branch",
    "FlowID": branch_flow_id,
    "Description": "New Branch",
    "BranchLogic":
    {
        "0": {},
        "Type": "BooleanExpression"
    },
    "Flow":
    [
      {
        "Type": "EmbeddedData",
        "FlowID": data_flow_id,
        "EmbeddedData":
        [
          {
            "Description": "term",
            "Type": "Custom",
            "Field": "term",
            "VariableType": "String",
            "DataVisibility":
            [],
            "AnalyzeText": False,
            "Value": question[question_number_index] + " " + question[term_index].lower()
          },
          {
            "Description": "gc",
            "Type": "Custom",
            "Field": "gc",
            "VariableType": "String",
            "DataVisibility":
            [],
            "AnalyzeText": False,
            "Value": "2"
          }
        ]
      },
      {
        "Type": "Standard",
        "ID": preview_term_id,
        "FlowID": "FL_11",
        "Autofill":
        []
      }, 
      {
        "Type": "EndSurvey",
        "FlowID": term_flow_id
      }
    ]
  }

  cur_term_block["BranchLogic"] = buildDisplayLogic(question,cur_question, qsf_output, True)

  #Add branch to flow
  qsf_output['SurveyElements'][1]["Payload"]["Flow"].insert(-2,cur_term_block)
  flow_count = {
    "Count":cur_flow_index
  }
  qsf_output['SurveyElements'][1]["Payload"]["Properties"] = flow_count

  #Add skip logic
  cur_question = buildSkipLogic(question, cur_question, qsf_output)

  return cur_question

def buildDisplayLogic(question, cur_question, qsf_output, from_term):
  #This function builds display logic as well as branch logic (the from_term bool)
  if from_term == False:
    logic_index = display_logic_index
  else:
    logic_index = term_index

  if question[logic_index] == "":
    return cur_question

  display_logic_value = {
    "0": {}
  }
  
  if comma_new_line == "comma":
    display_logics = question[logic_index].split(";")
  else:
    display_logics = question[logic_index].split("\n")

  for display_logic_iteration, display_logic in enumerate(display_logics):
    cur_display_logic = resetDisplayLogic()

    if from_term == False:
      cur_export_tag = display_logics[display_logic_iteration].split("is",1)[0].strip()
    else:
      cur_export_tag = cur_question["PrimaryAttribute"]

    if display_logic_iteration > 0:
      if from_term == False:
        conjunction = cur_export_tag.split()[0]
        cur_export_tag = cur_export_tag.split(' ', 1)[1]
      else:
        conjunction = display_logics[display_logic_iteration].split("is",1)[0].strip()

      cur_display_logic["Conjuction"] = conjunction.capitalize()

    cur_choice_index = display_logics[display_logic_iteration].split()[-1].strip()
    if "is not" in display_logics[display_logic_iteration].lower():
      Operator = "NotSelected"
    else:
      Operator = "Selected"

    cur_display_logic["Operator"] = Operator

    if from_term == False:
      for question_iteration, question in enumerate(qsf_output["SurveyElements"]):
        if "DataExportTag" in question["Payload"] and question["Payload"]["DataExportTag"] == cur_export_tag:
          QuestionID = question["PrimaryAttribute"]
          ChoiceLocator = "q://" + QuestionID + "/SelectableChoice/" + cur_choice_index
          continue
    else:
      QuestionID = cur_question["PrimaryAttribute"]
      ChoiceLocator = "q://" + cur_question["PrimaryAttribute"] + "/SelectableChoice/" + cur_choice_index

    cur_display_logic["QuestionID"] = QuestionID
    cur_display_logic["ChoiceLocator"] = ChoiceLocator
    cur_display_logic["QuestionIDFromLocator"] = QuestionID
    cur_display_logic["LeftOperand"] = ChoiceLocator
    display_logic_value["0"][str(display_logic_iteration)] = cur_display_logic

  display_logic_value["0"]["Type"] = "If"
  display_logic_value["Type"] = "BooleanExpression"

  if from_term == False:
    display_logic_value["inPage"] = False
    cur_question["Payload"]["DisplayLogic"] = display_logic_value
    return cur_question
  else:
    return display_logic_value

def addPreviewBlocks(qsf_output):
  global final_question_id
  global preview_term_id
  global preview_variables_id

  #Build preview: term question
  cur_question_id = "QID" + str(final_question_id + 2)
  preview_term_question["PrimaryAttribute"] = cur_question_id
  preview_term_question["Payload"]["QuestionID"] = cur_question_id
  qsf_output["SurveyElements"].append(preview_term_question)

  #Build preview: term block
  preview_block = resetPreviewBlock()
  preview_block["Description"] = "Preview: Term"
  preview_block["ID"] = preview_term_id
  preview_block["BlockElements"][0]["QuestionID"] = cur_question_id
  qsf_output["SurveyElements"][0]["Payload"].append(preview_block)

  #Build preview: variables question
  cur_question_id = "QID" + str(final_question_id + 3)
  preview_variables_question["PrimaryAttribute"] = cur_question_id
  preview_variables_question["Payload"]["QuestionID"] = cur_question_id
  qsf_output["SurveyElements"].append(preview_variables_question)

  #Build preview: variables block
  preview_block = resetPreviewBlock()
  preview_block["Description"] = "Preview: Variables"
  preview_block["ID"] = preview_variables_id
  preview_block["BlockElements"][0]["QuestionID"] = cur_question_id
  qsf_output["SurveyElements"][0]["Payload"].append(preview_block)

  return qsf_output

def createQuestions(qsf_input, qsf_output):
  #Used to know the final id to insert the preview blocks
  global final_question_id

  for question_iteration, question in enumerate(qsf_input[1:]):
    final_question_id = question_iteration

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
    cur_question = buildDisplayLogic(question, cur_question, qsf_output, False)

    qsf_output['SurveyElements'].append(cur_question)

    # Add question to block
    qsf_output = addQuestionToBlock(question_iteration, qsf_output, question, qsf_input)

    #Build terms
    cur_question = buildTerms(question, cur_question, qsf_output)

  #Add preview blocks
  qsf_output = addPreviewBlocks(qsf_output)
  return qsf_output

def convertCsvToQsf(qsf_output):
  with open('output.qsf', 'w') as outfile:
      json.dump(qsf_output, outfile)