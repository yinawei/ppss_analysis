from .image import *
import pandas as pd
import json

current_directory = os.path.dirname(__file__)
# print("current path: ", current_directory)

annotation = image(current_directory + "/annotation_25.nrrd")
bs_level = pd.read_csv(current_directory + "/bs_level.csv", sep=',', index_col=0)
with open(current_directory + "/dict_to_selected.json") as f:
    dict_to_selected = json.loads(f.read())

keys_list = list(dict_to_selected.keys())
for k in keys_list:
    dict_to_selected[int(k)] = dict_to_selected[k]
    del dict_to_selected[k]


def id_to_name(region_ID):
    # region_name can be either Abbreviation (checked first) or description
    if region_ID in bs_level.index.tolist():
        return bs_level.loc[region_ID, 'Abbreviation']
    else:
        print("Cannot find any regions with ID %s." % region_ID)


def get_node_region(point, scaled=False, detail_info=False):
    p = point[['x', 'y', 'z']].copy()
    if not scaled:
        p['x'] = p['x'] / annotation.space['x']
        p['y'] = p['y'] / annotation.space['y']
        p['z'] = p['z'] / annotation.space['z']
    p = p.round(0).astype(int)
    if ((p.x.iloc[0] >= 0) & (p.x.iloc[0] < annotation.size['x']) &
            (p.y.iloc[0] >= 0) & (p.y.iloc[0] < annotation.size['y']) &
            (p.z.iloc[0] >= 0) & (p.z.iloc[0] < annotation.size['z'])
    ):
        region_id = annotation.array[p.x.iloc[0],
        p.y.iloc[0],
        p.z.iloc[0]
        ]
        if region_id in list(dict_to_selected.keys()):
            # region_id = dict_to_selected[region_id]
            detail_region = id_to_name(region_id)
            region = id_to_name(dict_to_selected[region_id])

            if detail_info:
                return [region, detail_region]
            else:
                return region

        # if two_label:
        #     detail_id = region_id.copy()
        #     rough_id = nmt.bs.dict_to_selected[detail_id]
        #     return [nmt.bs.id_to_name(detail_id), nmt.bs.id_to_name(rough_id)]

    return 'unknow'


def add_region(df):
    df['region'] = 0
    df['region'] = df.apply(lambda r: get_node_region(pd.DataFrame({'x': [r.x], 'y': [r.y], 'z': [r.z]})),
                            axis=1)

    return df
