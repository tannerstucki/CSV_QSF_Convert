qsf_output['SurveyElements'].append({
         "SurveyID":"SV_7QjmSDFoYo2LpoG",
         "Element":"BL",
         "PrimaryAttribute":"Survey Blocks",
         "SecondaryAttribute":None,
         "TertiaryAttribute":None,
         "Payload":[
            {
               "Type":"Default",
               "Description":"Block 1",
               "ID":"BL_9z7Q1lmkbG3GQIK",
               "BlockElements":[
                  {
                     "Type":"Question",
                     "QuestionID":"QID1"
                  },
                  {
                     "Type":"Question",
                     "QuestionID":"QID2"
                  }
               ]
            },
            {
               "Type":"Trash",
               "Description":"Trash",
               "ID":"BL_0DpCODigcVsDj5s"
            },
            {
               "Type":"Standard",
               "SubType":"",
               "Description":"Block 2",
               "ID":"BL_aWsJA19Jx1l6yUK",
               "BlockElements":[
                  {
                     "Type":"Question",
                     "QuestionID":"QID3"
                  }
               ]
            }
         ]
      })

qsf_output['SurveyElements'].append({
         "SurveyID":"SV_7QjmSDFoYo2LpoG",
         "Element":"FL",
         "PrimaryAttribute":"Survey Flow",
         "SecondaryAttribute":None,
         "TertiaryAttribute":None,
         "Payload":{
            "Flow":[
               {
                  "ID":"BL_9z7Q1lmkbG3GQIK",
                  "Type":"Block",
                  "FlowID":"FL_2"
               },
               {
                  "ID":"BL_aWsJA19Jx1l6yUK",
                  "Type":"Standard",
                  "FlowID":"FL_3"
               }
            ],
            "Properties":{
               "Count":3
            },
            "FlowID":"FL_1",
            "Type":"Root"
         }
      })

qsf_output['SurveyElements'].append({
         "SurveyID":"SV_7QjmSDFoYo2LpoG",
         "Element":"SO",
         "PrimaryAttribute":"Survey Options",
         "SecondaryAttribute":None,
         "TertiaryAttribute":None,
         "Payload":{
            "BackButton":"true",
            "SaveAndContinue":"true",
            "SurveyProtection":"PublicSurvey",
            "BallotBoxStuffingPrevention":"false",
            "NoIndex":"Yes",
            "SecureResponseFiles":"true",
            "SurveyExpiration":"None",
            "SurveyTermination":"DefaultMessage",
            "Header":"",
            "Footer":"",
            "ProgressBarDisplay":"None",
            "PartialData":"+1 week",
            "ValidationMessage":"",
            "PreviousButton":" \u2190 ",
            "NextButton":" \u2192 ",
            "SurveyTitle":"QSF Default Upload",
            "SkinLibrary":"qxm",
            "SkinType":"MQ",
            "Skin":"minimal-wd1",
            "NewScoring":1
         }
      })

qsf_output['SurveyElements'].append({
         "SurveyID":"SV_7QjmSDFoYo2LpoG",
         "Element":"SQ",
         "PrimaryAttribute":"QID1",
         "SecondaryAttribute":"What is your favorite food?",
         "TertiaryAttribute":None,
         "Payload":{
            "QuestionText":"What is your favorite food?",
            "DataExportTag":"Q1",
            "QuestionType":"MC",
            "Selector":"SAVR",
            "SubSelector":"TX",
            "Configuration":{
               "QuestionDescriptionOption":"UseText"
            },
            "QuestionDescription":"What is your favorite food?",
            "Choices":{
               "1":{
                  "Display":"Burgers"
               },
               "2":{
                  "Display":"Tacos"
               },
               "3":{
                  "Display":"Pizza"
               }
            },
            "ChoiceOrder":[
               "1",
               "2",
               "3"
            ],
            "Validation":{
               "Settings":{
                  "ForceResponse":"OFF",
                  "Type":"None"
               }
            },
            "Language":[
               
            ],
            "NextChoiceId":4,
            "NextAnswerId":1,
            "QuestionID":"QID1"
         }
      })

qsf_output['SurveyElements'].append({
         "SurveyID":"SV_7QjmSDFoYo2LpoG",
         "Element":"SQ",
         "PrimaryAttribute":"QID2",
         "SecondaryAttribute":"What sports do you play?",
         "TertiaryAttribute":None,
         "Payload":{
            "QuestionText":"What sports do you play?",
            "DefaultChoices":False,
            "DataExportTag":"Q2",
            "QuestionType":"MC",
            "Selector":"MAVR",
            "SubSelector":"TX",
            "Configuration":{
               "QuestionDescriptionOption":"UseText"
            },
            "QuestionDescription":"What sports do you play?",
            "Choices":{
               "1":{
                  "Display":"Basketball"
               },
               "2":{
                  "Display":"Football"
               },
               "3":{
                  "Display":"Tennis"
               }
            },
            "ChoiceOrder":[
               "1",
               "2",
               "3"
            ],
            "Validation":{
               "Settings":{
                  "ForceResponse":"OFF",
                  "Type":"None"
               }
            },
            "GradingData":[
               
            ],
            "Language":[
               
            ],
            "NextChoiceId":4,
            "NextAnswerId":1,
            "QuestionID":"QID2"
         }
      })

qsf_output['SurveyElements'].append({
         "SurveyID":"SV_7QjmSDFoYo2LpoG",
         "Element":"SQ",
         "PrimaryAttribute":"QID3",
         "SecondaryAttribute":"Where are you from?",
         "TertiaryAttribute":None,
         "Payload":{
            "QuestionText":"Where are you from?",
            "DefaultChoices":False,
            "DataExportTag":"Q3",
            "QuestionType":"TE",
            "Selector":"SL",
            "Configuration":{
               "QuestionDescriptionOption":"UseText"
            },
            "QuestionDescription":"Where are you from?",
            "Validation":{
               "Settings":{
                  "ForceResponse":"OFF",
                  "Type":"None"
               }
            },
            "GradingData":[
               
            ],
            "Language":[
               
            ],
            "NextChoiceId":4,
            "NextAnswerId":1,
            "SearchSource":{
               "AllowFreeResponse":"false"
            },
            "QuestionID":"QID3"
         }
      })