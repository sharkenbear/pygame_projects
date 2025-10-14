import json

def set_file (full_colour_grid):

    # read JSON file and parse contents
    with open('grid_file.json', 'r') as file:
        python_obj = json.load(file)

    file_name = python_obj['name']
    file_type = python_obj['type']

    # defines the new contents
    sprite = {
            "name" : file_name,
            "type" : file_type,
            "content_0" : str(full_colour_grid[0]),
            "content_1" : str(full_colour_grid[1]),
            "content_2" : str(full_colour_grid[2]),
            "content_3" : str(full_colour_grid[3]),
            "content_4" : str(full_colour_grid[4]),
            "content_5" : str(full_colour_grid[5]),
            "content_6" : str(full_colour_grid[6]),
            "content_7" : str(full_colour_grid[7]),
            "content_8" : str(full_colour_grid[8]),
            "content_9" : str(full_colour_grid[9]),
            "content_10" : str(full_colour_grid[10]),
            "content_11" : str(full_colour_grid[11]),
            "content_12" : str(full_colour_grid[12]),
            "content_13" : str(full_colour_grid[13]),
            "content_14" : str(full_colour_grid[14]),
            "content_15" : str(full_colour_grid[15]),
            "content_16" : str(full_colour_grid[16]),
            "content_17" : str(full_colour_grid[17]),
            "content_18" : str(full_colour_grid[18]),
            "content_19" : str(full_colour_grid[19]),
            "content_20" : str(full_colour_grid[20]),
            "content_21" : str(full_colour_grid[21]),
            "content_22" : str(full_colour_grid[22]),
            "content_23" : str(full_colour_grid[23]),
            "content_24" : str(full_colour_grid[24]),
            "content_25" : str(full_colour_grid[25]),
            "content_26" : str(full_colour_grid[26]),
            "content_27" : str(full_colour_grid[27]),
            "content_28" : str(full_colour_grid[28]),
            "content_29" : str(full_colour_grid[29]),
            "content_30" : str(full_colour_grid[30]),
            "content_31" : str(full_colour_grid[31]),
            "content_32" : str(full_colour_grid[32]),
            "content_33" : str(full_colour_grid[33]),
            "content_34" : str(full_colour_grid[34]),
            "content_35" : str(full_colour_grid[35]),
            "content_36" : str(full_colour_grid[36]),
            "content_37" : str(full_colour_grid[37]),
            "content_38" : str(full_colour_grid[38]),
            "content_39" : str(full_colour_grid[39]),
            "content_40" : str(full_colour_grid[40]),
            "content_41" : str(full_colour_grid[41]),
            "content_42" : str(full_colour_grid[42]),
            "content_43" : str(full_colour_grid[43]),
            "content_44" : str(full_colour_grid[44]),
            "content_45" : str(full_colour_grid[45]),
            "content_46" : str(full_colour_grid[46]),
            "content_47" : str(full_colour_grid[47]),
            "content_48" : str(full_colour_grid[48]),
            "content_49" : str(full_colour_grid[49]),
            "content_50" : str(full_colour_grid[50]),
            "content_51" : str(full_colour_grid[51]),
            "content_52" : str(full_colour_grid[52]),
            "content_53" : str(full_colour_grid[53]),
            "content_54" : str(full_colour_grid[54]),
            "content_55" : str(full_colour_grid[55]),
            "content_56" : str(full_colour_grid[56]),
            "content_57" : str(full_colour_grid[57]),
            "content_58" : str(full_colour_grid[58]),
            "content_59" : str(full_colour_grid[59]),
            "content_60" : str(full_colour_grid[60]),
            "content_61" : str(full_colour_grid[61]),
            "content_62" : str(full_colour_grid[62]),
            "content_63" : str(full_colour_grid[63]),
        }

    # for key in sprite:
        # sprite[key] += "\nNew Line"

    # dumps the new contents to the file
    with open('grid_file.json', 'w') as file:
        json.dump(sprite, file, indent = 4)