
import json
import uuid

# Input JSON data
data = {
  "root": {
    "blocks": [
      {
        "id": "subdir_1",
        "type": "SUBDIRECTORY",
        "name": "backend",
        "x": 1315.0,
        "y": 1365.0,
        "width": 250.0,
        "height": 100.0,
        "metadata": {},
        "exists": True
      },
      {
        "id": "subdir_2",
        "type": "SUBDIRECTORY",
        "name": "frontends",
        "x": 1650.0,
        "y": 1366.0,
        "width": 250.0,
        "height": 100.0,
        "metadata": {},
        "exists": True
      },
      {
        "id": "subdir_3",
        "type": "SUBDIRECTORY",
        "name": "tasks",
        "x": 1320.0,
        "y": 1527.0,
        "width": 238.0,
        "height": 99.0,
        "metadata": {
          "alias": "Workers and Tasks"
        },
        "exists": True
      },
      {
        "id": "subdir_4",
        "type": "SUBDIRECTORY",
        "name": "doc_examples",
        "x": 1650.0,
        "y": 1523.0,
        "width": 247.0,
        "height": 105.0,
        "metadata": {
          "alias": "Example Documents"
        },
        "exists": True
      }
    ],
    "connections": []
  },
  "root/backend": {
    "blocks": [
      {
        "id": "subdir_1",
        "type": "SUBDIRECTORY",
        "name": "ai_sheet_grading",
        "x": 1081.0,
        "y": 1305.0,
        "width": 254.0,
        "height": 97.0,
        "metadata": {
          "alias": "AI Sheet Grading Module"
        },
        "exists": True
      },
      {
        "id": "subdir_2",
        "type": "SUBDIRECTORY",
        "name": "integrations",
        "x": 1412.0,
        "y": 1308.0,
        "width": 250.0,
        "height": 100.0,
        "metadata": {},
        "exists": True
      },
      {
        "id": "subdir_3",
        "type": "SUBDIRECTORY",
        "name": "sheet_downloading",
        "x": 1083.0,
        "y": 1454.0,
        "width": 250.0,
        "height": 100.0,
        "metadata": {},
        "exists": True
      }
    ],
    "connections": []
  },
  "root/frontend": {
    "blocks": [],
    "connections": []
  },
  "root/frontends": {
    "blocks": [
      {
        "id": "subdir_1",
        "type": "SUBDIRECTORY",
        "name": "frontend_dev",
        "x": 1155.0,
        "y": 1379.0,
        "width": 250.0,
        "height": 100.0,
        "metadata": {},
        "exists": True
      },
      {
        "id": "subdir_2",
        "type": "SUBDIRECTORY",
        "name": "frontend_enduser",
        "x": 1459.0,
        "y": 1376.0,
        "width": 250.0,
        "height": 100.0,
        "metadata": {},
        "exists": True
      }
    ],
    "connections": []
  },
  "root/tasks": {
    "blocks": [],
    "connections": []
  },
  "root/backend/ai_sheet_grading": {
    "blocks": [
      {
        "id": "subdir_1",
        "type": "SUBDIRECTORY",
        "name": "answer_sheet_extraction",
        "x": 975.0325000000003,
        "y": 726.4425000000003,
        "width": 250.0,
        "height": 100.0,
        "metadata": {},
        "exists": True
      },
      {
        "id": "subdir_2",
        "type": "SUBDIRECTORY",
        "name": "schema_operations",
        "x": 1281.835,
        "y": 724.1200000000001,
        "width": 250.0,
        "height": 100.0,
        "metadata": {},
        "exists": True
      },
      {
        "id": "func_6",
        "type": "FUNCTION",
        "name": "process_question_sheets()",
        "x": 566.2643227151564,
        "y": 1066.616075728594,
        "width": 232.0,
        "height": 60.0,
        "metadata": {
          "functionName": "process_question_sheets",
          "filePath": "backend\\ai_sheet_grading\\stage1_process_question_papers.py",
          "lineNumber": 12,
          "alias": "Process Question Sheets"
        },
        "exists": True
      },
      {
        "id": "other_7",
        "type": "OTHER",
        "name": "Main Function",
        "x": 584.7793227151562,
        "y": 1016.361075728593,
        "width": 196.0324999999999,
        "height": 50.0,
        "metadata": {},
        "exists": True
      },
      {
        "id": "func_8",
        "type": "FUNCTION",
        "name": "extract_schema()",
        "x": 485.1582593881243,
        "y": 1174.5794216643224,
        "width": 392.0,
        "height": 60.0,
        "metadata": {
          "functionName": "extract_schema",
          "filePath": "backend\\ai_sheet_grading\\stage1_process_question_papers.py",
          "lineNumber": 5,
          "alias": "Call LLM: Extract Schema from Question Paper"
        },
        "exists": True
      },
      {
        "id": "func_9",
        "type": "FUNCTION",
        "name": "repair_json()",
        "x": 867.1272385941735,
        "y": 1245.9757260121482,
        "width": 150.0,
        "height": 60.0,
        "metadata": {
          "functionName": "repair_json",
          "filePath": "backend\\ai_sheet_grading\\stage1_process_question_papers.py",
          "lineNumber": 6,
          "alias": "Repair Json"
        },
        "exists": True
      },
      {
        "id": "func_10",
        "type": "FUNCTION",
        "name": "match_question_sheet_identifiers_to_rubric()",
        "x": 493.5528657208273,
        "y": 1355.162127004586,
        "width": 378.0,
        "height": 60.0,
        "metadata": {
          "functionName": "match_question_sheet_identifiers_to_rubric",
          "filePath": "backend\\ai_sheet_grading\\stage1_process_question_papers.py",
          "lineNumber": 8,
          "alias": "Call LLM: Match Q Paper identifeirs to Rubric"
        },
        "exists": True
      },
      {
        "id": "func_11",
        "type": "FUNCTION",
        "name": "repair_json()",
        "x": 880.5785949268758,
        "y": 1424.712323365645,
        "width": 150.0,
        "height": 60.0,
        "metadata": {
          "functionName": "repair_json",
          "filePath": "backend\\ai_sheet_grading\\stage1_process_question_papers.py",
          "lineNumber": 6,
          "alias": "Repair Json"
        },
        "exists": True
      },
      {
        "id": "func_12",
        "type": "FUNCTION",
        "name": "cleanup_questions_tree()",
        "x": 844.976648802113,
        "y": 1525.3153635357774,
        "width": 222.0,
        "height": 60.0,
        "metadata": {
          "functionName": "cleanup_questions_tree",
          "filePath": "backend\\ai_sheet_grading\\stage1_process_question_papers.py",
          "lineNumber": 7,
          "alias": "Cleanup Questions Tree"
        },
        "exists": True
      },
      {
        "id": "func_13",
        "type": "FUNCTION",
        "name": "clear_branch_node_marking()",
        "x": 822.9042629325475,
        "y": 1615.0001246416384,
        "width": 265.0,
        "height": 60.0,
        "metadata": {
          "functionName": "clear_branch_node_marking",
          "filePath": "backend\\ai_sheet_grading\\stage1_process_question_papers.py",
          "lineNumber": 7,
          "alias": "Clear Branch nodes markings"
        },
        "exists": True
      },
      {
        "id": "func_14",
        "type": "FUNCTION",
        "name": "change_schema_key()",
        "x": 819.5322977151561,
        "y": 1711.7932694785939,
        "width": 270.0,
        "height": 60.0,
        "metadata": {
          "functionName": "change_schema_key",
          "filePath": "backend\\ai_sheet_grading\\stage1_process_question_papers.py",
          "lineNumber": 7,
          "alias": "Update \"text\" key to \"Question\""
        },
        "exists": True
      },
      {
        "id": "func_15",
        "type": "FUNCTION",
        "name": "extract_questions()",
        "x": 513.4396727151562,
        "y": 1832.5375194785927,
        "width": 347.0,
        "height": 60.0,
        "metadata": {
          "functionName": "extract_questions",
          "filePath": "backend\\ai_sheet_grading\\question_sheet_extraction.py",
          "lineNumber": 89,
          "alias": "Call LLM: Extract Questions from QPaper"
        },
        "exists": True
      },
      {
        "id": "func_16",
        "type": "FUNCTION",
        "name": "repair_json()",
        "x": 850.406060215156,
        "y": 1952.395694478593,
        "width": 200.0,
        "height": 80.0,
        "metadata": {
          "functionName": "repair_json",
          "filePath": "backend\\ai_sheet_grading\\stage1_process_question_papers.py",
          "lineNumber": 6
        },
        "exists": True
      },
      {
        "id": "func_17",
        "type": "FUNCTION",
        "name": "change_schema_key()",
        "x": 796.1868664651558,
        "y": 2080.073150728592,
        "width": 310.0,
        "height": 60.0,
        "metadata": {
          "functionName": "change_schema_key",
          "filePath": "backend\\ai_sheet_grading\\stage1_process_question_papers.py",
          "lineNumber": 7,
          "alias": "Change \"marks\" key to \"max marks\""
        },
        "exists": True
      },
      {
        "id": "other_18",
        "type": "OTHER",
        "name": "Question Paper Extraction Completed",
        "x": 519.843878965156,
        "y": 2214.7466319785917,
        "width": 324.1794437499998,
        "height": 67.7569562499998,
        "metadata": {},
        "exists": True
      },
      {
        "id": "func_19",
        "type": "FUNCTION",
        "name": "process_model_answers()",
        "x": 1258.5671512031251,
        "y": 1066.2827100468742,
        "width": 215.0,
        "height": 60.0,
        "metadata": {
          "functionName": "process_model_answers",
          "filePath": "backend\\ai_sheet_grading\\stage2_process_model_papers.py",
          "lineNumber": 9,
          "alias": "Process Model APaper"
        },
        "exists": True
      },
      {
        "id": "other_20",
        "type": "OTHER",
        "name": "Main Function",
        "x": 1283.6946512031247,
        "y": 1016.027710046875,
        "width": 161.64750000000004,
        "height": 50.0,
        "metadata": {},
        "exists": True
      },
      {
        "id": "func_21",
        "type": "FUNCTION",
        "name": "model_apaper_answers_extraction()",
        "x": 1209.6346512031243,
        "y": 1173.405210046875,
        "width": 332.0,
        "height": 60.0,
        "metadata": {
          "functionName": "model_apaper_answers_extraction",
          "filePath": "backend\\ai_sheet_grading\\stage2_process_model_papers.py",
          "lineNumber": 7,
          "alias": "Call LLM: Extract Answers from Apaper"
        },
        "exists": True
      },
      {
        "id": "func_22",
        "type": "FUNCTION",
        "name": "repair_json()",
        "x": 1561.1621512031245,
        "y": 1240.4977100468748,
        "width": 150.0,
        "height": 60.0,
        "metadata": {
          "functionName": "repair_json",
          "filePath": "backend\\ai_sheet_grading\\stage2_process_model_papers.py",
          "lineNumber": 6,
          "alias": "Repair Json"
        },
        "exists": True
      },
      {
        "id": "func_23",
        "type": "FUNCTION",
        "name": "transform_question_identifiers()",
        "x": 1441.0721512031243,
        "y": 1338.717710046875,
        "width": 387.0,
        "height": 60.0,
        "metadata": {
          "functionName": "transform_question_identifiers",
          "filePath": "backend\\ai_sheet_grading\\stage2_process_model_papers.py",
          "lineNumber": 5,
          "alias": "Transform Question Identifiers to that in Rubric"
        },
        "exists": True
      },
      {
        "id": "other_24",
        "type": "OTHER",
        "name": "Question Paper updated with Model Answers",
        "x": 1204.3446512031244,
        "y": 1476.257710046875,
        "width": 365.3125,
        "height": 81.32249999999999,
        "metadata": {},
        "exists": True
      },
      {
        "id": "func_22a",
        "type": "FUNCTION",
        "name": "evaluate_student_answer_sheets()",
        "x": 2042.979192109375,
        "y": 1066.3781395624999,
        "width": 228.0,
        "height": 60.0,
        "metadata": {
          "functionName": "evaluate_student_answer_sheets",
          "filePath": "backend\\ai_sheet_grading\\stage3_evaluate_students.py",
          "lineNumber": 12,
          "alias": "Evaluate Student APaper"
        },
        "exists": True
      },
      {
        "id": "other_23",
        "type": "OTHER",
        "name": "Main Function",
        "x": 2075.3183421093754,
        "y": 1017.5932708124999,
        "width": 166.6500000000001,
        "height": 50.0,
        "metadata": {},
        "exists": True
      },
      {
        "id": "func_24",
        "type": "FUNCTION",
        "name": "apaper_answers_extraction()",
        "x": 1958.0183421093745,
        "y": 1171.6932708124993,
        "width": 403.0,
        "height": 60.0,
        "metadata": {
          "functionName": "apaper_answers_extraction",
          "filePath": "backend\\ai_sheet_grading\\stage3_evaluate_students.py",
          "lineNumber": 7,
          "alias": "Call LLM: Extract Answers from Candidate Paper"
        },
        "exists": True
      },
      {
        "id": "func_25",
        "type": "FUNCTION",
        "name": "repair_json()",
        "x": 2374.3183421093754,
        "y": 1241.8432708125,
        "width": 150.0,
        "height": 60.0,
        "metadata": {
          "functionName": "repair_json",
          "filePath": "backend\\ai_sheet_grading\\stage3_evaluate_students.py",
          "lineNumber": 6,
          "alias": "Repair Json"
        },
        "exists": True
      },
      {
        "id": "func_26",
        "type": "FUNCTION",
        "name": "transform_question_identifiers()",
        "x": 2255.8683421093756,
        "y": 1339.5932708125,
        "width": 387.0,
        "height": 60.0,
        "metadata": {
          "functionName": "transform_question_identifiers",
          "filePath": "backend\\ai_sheet_grading\\stage3_evaluate_students.py",
          "lineNumber": 5,
          "alias": "Transform Question Identifiers to that in Rubric"
        },
        "exists": True
      },
      {
        "id": "func_27",
        "type": "FUNCTION",
        "name": "merge_answers()",
        "x": 2260.261820370245,
        "y": 1445.2867490733704,
        "width": 382.0,
        "height": 60.0,
        "metadata": {
          "functionName": "merge_answers",
          "filePath": "backend\\ai_sheet_grading\\stage3_evaluate_students.py",
          "lineNumber": 5,
          "alias": "Merge Candidate JSON with Model Ans JSON"
        },
        "exists": True
      },
      {
        "id": "func_28",
        "type": "FUNCTION",
        "name": "grade_answers()",
        "x": 2014.9994942832893,
        "y": 1569.8701700373656,
        "width": 294.0,
        "height": 60.0,
        "metadata": {
          "functionName": "grade_answers",
          "filePath": "backend\\ai_sheet_grading\\answers_grading.py",
          "lineNumber": 70,
          "alias": "Call LLM: Grade Candidate Paper"
        },
        "exists": True
      },
      {
        "id": "func_29",
        "type": "FUNCTION",
        "name": "repair_json()",
        "x": 2385.2009162302993,
        "y": 1688.7823493851909,
        "width": 150.0,
        "height": 60.0,
        "metadata": {
          "functionName": "repair_json",
          "filePath": "backend\\ai_sheet_grading\\stage3_evaluate_students.py",
          "lineNumber": 6,
          "alias": "Repair JSON"
        },
        "exists": True
      },
      {
        "id": "other_30",
        "type": "OTHER",
        "name": "Final Extracted Paper with Candidate Answers and AI Grade",
        "x": 1924.6422205781248,
        "y": 1805.225723921875,
        "width": 470.25,
        "height": 71.95000000000005,
        "metadata": {},
        "exists": True
      }
    ],
    "connections": [
      {
        "from": "func_12",
        "to": "func_13",
        "from_side": "bottom",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_8",
        "to": "func_9",
        "from_side": "right",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_10",
        "to": "func_11",
        "from_side": "right",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_9",
        "to": "func_10",
        "from_side": "bottom",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_11",
        "to": "func_12",
        "from_side": "bottom",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_13",
        "to": "func_14",
        "from_side": "bottom",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_14",
        "to": "func_15",
        "from_side": "bottom",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_15",
        "to": "func_16",
        "from_side": "bottom",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_16",
        "to": "func_17",
        "from_side": "bottom",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_17",
        "to": "other_18",
        "from_side": "bottom",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_23",
        "to": "other_24",
        "from_side": "bottom",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_6",
        "to": "func_19",
        "from_side": "right",
        "to_side": "left",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_24",
        "to": "func_25",
        "from_side": "right",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_25",
        "to": "func_26",
        "from_side": "bottom",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_19",
        "to": "func_22a",
        "from_side": "right",
        "to_side": "left",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_26",
        "to": "func_27",
        "from_side": "bottom",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_27",
        "to": "func_28",
        "from_side": "bottom",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_28",
        "to": "func_29",
        "from_side": "bottom",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_29",
        "to": "other_30",
        "from_side": "bottom",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_21",
        "to": "func_22",
        "from_side": "right",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      },
      {
        "from": "func_22",
        "to": "func_23",
        "from_side": "bottom",
        "to_side": "top",
        "flow_type": "one_way",
        "line_style": "solid",
        "line_color": {
          "r": 100,
          "g": 100,
          "b": 100
        }
      }
    ]
  },
  "root/backend/integrations": {
    "blocks": [],
    "connections": []
  },
  "root/backend/sheet_downloading": {
    "blocks": [],
    "connections": []
  },
  "root/backend/doc_examples": {
    "blocks": [],
    "connections": []
  },
  "root/doc_examples": {
    "blocks": [],
    "connections": []
  },
  "root/frontends/frontend_dev": {
    "blocks": [],
    "connections": []
  },
  "root/frontends/frontend_enduser": {
    "blocks": [],
    "connections": []
  },
  "root/backend/ai_sheet_grading/answer_sheet_extraction": {
    "blocks": [],
    "connections": []
  },
  "root/backend/ai_sheet_grading/schema_operations": {
    "blocks": [],
    "connections": []
  },
  "_root_path": "C:/Work/Codes/auto_score_generation"
}

# Create mapping for old IDs to new UUIDs
id_mapping = {}

def replace_id(old_id):
    if old_id not in id_mapping:
        prefix = old_id.rsplit('_', 1)[0]
        id_mapping[old_id] = f"{prefix}_{uuid.uuid4().hex}"
    return id_mapping[old_id]

# Process all blocks and update IDs
for key in data:
    if key == "_root_path":
        continue
    
    if "blocks" in data[key]:
        for block in data[key]["blocks"]:
            old_id = block["id"]
            block["id"] = replace_id(old_id)
    
    if "connections" in data[key]:
        for conn in data[key]["connections"]:
            if "from" in conn:
                conn["from"] = replace_id(conn["from"])
            if "to" in conn:
                conn["to"] = replace_id(conn["to"])

print(json.dumps(data, indent=2))