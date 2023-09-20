import numpy as np

mapping_dict = {
    'Alley': {'NA': 0, 'None': 0, 'Grvl': 1, 'Pave': 2},
    'BsmtCond': {'NA': 0, 'None': 0, 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5},
    'BsmtExposure': {'NA': 0, 'None': 0, 'No': 1, 'Mn': 2, 'Av': 3, 'Gd': 4},
    'BsmtFinType1': {'NA': 0, 'None': 0, 'Unf': 1, 'LwQ': 2, 'Rec': 3, 'BLQ': 4, 'ALQ': 5, 'GLQ': 6},
    'BsmtFinType2': {'NA': 0, 'None': 0, 'Unf': 1, 'LwQ': 2, 'Rec': 3, 'BLQ': 4, 'ALQ': 5, 'GLQ': 6},
    'BsmtQual': {'NA': 0, 'None': 0, 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5},
    'ExterCond': {'NA': 0, 'None': 0, 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5},
    'ExterQual': {'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5},
    'FireplaceQu': {'NA': 0, 'None': 0, 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5},
    'Functional': {'Sal': 1, 'Sev': 2, 'Maj2': 3, 'Maj1': 4, 'Mod': 5, 'Min2': 6, 'Min1': 7, 'Typ': 8},
    'GarageCond': {'NA': 0, 'None': 0, 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5},
    'GarageQual': {'NA': 0, 'None': 0, 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5},
    'HeatingQC': {'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5},
    'KitchenQual': {'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5},
    'LandSlope': {'Sev': 1, 'Mod': 2, 'Gtl': 3},
    'PavedDrive': {'N': 1, 'P': 2, 'Y': 3},
    'PoolQC': {'NA': 0, 'None': 0, 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4},
    'Street': {'NA': 0, 'None': 0, 'Grvl': 1, 'Pave': 2},
    'Utilities': {'ELO': 1, 'NoSeWa': 2, 'NoSewr': 3, 'AllPub': 4},
    'Neighborhood': {'NA': 0, 'None': 0, 'MeadowV': 1, 'IDOTRR': 1, 'BrDale': 1,
                     'OldTown': 2, 'Edwards': 2, 'BrkSide': 2,
                     'Sawyer': 3, 'Blueste': 3, 'SWISU': 3, 'NAmes': 3,
                     'NPkVill': 4, 'Mitchel': 4, 'SawyerW': 4,
                     'Gilbert': 5, 'NWAmes': 5, 'Blmngtn': 5,
                     'CollgCr': 6, 'ClearCr': 6, 'Crawfor': 6,
                     'Somerst': 8, 'Veenker': 8, 'Timber': 8,
                     'StoneBr': 10, 'NoRidge': 10, 'NridgHt': 10},
    'MSSubClass': {20: 'class20', 30: 'class30', 40: 'class40', 45: 'class45',
                   50: 'class50', 60: 'class60', 70: 'class70', 75: 'class75',
                   80: 'class80', 85: 'class85', 90: 'class90', 120: 'class120',
                   150: 'class150', 160: 'class160', 180: 'class180', 190: 'class190'}
}

def apply_log(value):
    if(isinstance(value, str)):
        value = float(value)

    if value == 0:
      return value

    return np.log1p(value)

def check_if_log(feature):
    log_features = ['LotFrontage', 'LotArea', 'Street', 'Alley', 'Utilities', 'LandSlope', 'Neighborhood',
                    'OverallCond', 'MasVnrArea', 'ExterQual', 'ExterCond', 'BsmtQual', 'BsmtCond', 'BsmtExposure',
                    'BsmtFinSF1', 'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'HeatingQC', '1stFlrSF', '2ndFlrSF',
                    'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'HalfBath', 'KitchenAbvGr',
                    'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'GarageQual', 'GarageCond', 'PavedDrive', 'WoodDeckSF',
                    'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'PoolQC', 'MiscVal', 'Age',
                    'AgeGarage']
    return 1 if feature in log_features else 0


def get_mapped_value(category, value):
    if category in mapping_dict:
        value = mapping_dict[category].get(value, None)
        if check_if_log(category) and value != 0:
          return apply_log(value)

        return value
    else:
        return None
    
def check_if_exist(value):
  zone_list = ['RL', 'RM', 'FR2', 'Norm', 'PosA', 'BrkFace', 'Plywood', 'Wood', 'Detchd', 'Unf', 'ConLD', 'Normal']

  return 1 if value in  zone_list else 0

def preprocess(form_data, test=False):
    MSSubClass = '30' if test else form_data['mssubclass']
    MSZoning = 'RL' if test else form_data['mszoning']
    LotConfig = '' if test else form_data['lotconfig']
    Condition1 ='' if test else form_data['condition1']
    Exterior1st = '' if test else form_data['exterior1st']
    Foundation ='' if test else form_data['foundation']
    GarageType = '' if test else form_data['garagetype']
    GarageFinish ='' if test else form_data['garagefinish']
    SaleType = '' if test else form_data['saletype']
    SaleCondition = '' if test else form_data['salecondition']
    CentralAir = 'N' if test else form_data['centralair']
    Neighborhood = 'MeadowV' if test else form_data['neighborhood']
    Functional='Sev' if test else form_data['functional']
    LotArea=1 if test else form_data['lotarea']
    Alley = 'Pave' if test else form_data['alley']
    OverallQual = 8 if test else form_data['overallqual']
    OverallCond = 8 if test else form_data['overallcond']
    ExterQual='Ex' if test else form_data['exterqual']
    ExterCond='Po' if test else form_data['extercond']
    BsmtQual='Po' if test else form_data['bsmtqual']
    BsmtFinSF1=1 if test else form_data['bsmtfinsf1']
    BsmtExposure='Gd' if test else form_data['bsmtexposure']
    BsmtFinType1='Unf' if test else form_data['bsmtfintype1']
    BsmtFinType2='ALQ' if test else form_data['bsmtfintype2']
    BsmtUnfSF=1 if test else form_data['bsmtunfsf']
    TotalBsmtSF=8 if test else form_data['totalbsmtsf']
    stFlrSF =8 if test else form_data['1stflrsf']
    ndFlrSF=9 if test else form_data['2ndflrsf']
    GrLivArea=7 if test else form_data['grlivarea']
    BsmtFullBath=1 if test else form_data['bsmtfullbath']
    FullBath=2 if test else form_data['fullbath']
    KitchenQual='Ex' if test else form_data['kitchenqual']
    FireplaceQu='Ex' if test else form_data['fireplacequ']
    GarageCars=2 if test else form_data['garagecars']
    GarageQual='Fa' if test else form_data['garagequal']
    GarageCond='Ex' if test else form_data['garagecond']
    WoodDeckSF=2 if test else form_data['wooddecksf']
    OpenPorchSF=8 if test else form_data['openporchsf']
    EnclosedPorch=0 if test else form_data['enclosedporch']
    ScreenPorch=0 if test else form_data['screenporch']
    MoSold=9 if test else form_data['mosold']
    YrSold =2010 if test else form_data['yrsold']
    YearRemodAdd=2013 if test else form_data['yearremodadd']
    GarageYrBlt=0 if test else form_data['garageyrblt']
    YearBuilt=2000 if test else form_data['yearbuilt']

    return {
        'LotArea': apply_log(LotArea),
        'Alley': get_mapped_value('Alley', Alley),
        'Neighborhood': get_mapped_value('Neighborhood', Neighborhood),
        'OverallQual': float(OverallQual),
        'OverallCond': float(OverallCond),
        'ExterQual': get_mapped_value('ExterQual', ExterQual),
        'ExterCond': get_mapped_value('ExterCond', ExterCond),
        'BsmtQual': get_mapped_value('BsmtQual', BsmtQual),
        'BsmtExposure': get_mapped_value('BsmtExposure', BsmtExposure),
        'BsmtFinType1': get_mapped_value('BsmtFinType1', BsmtFinType1),
        'BsmtFinSF1': apply_log(BsmtFinSF1),
        'BsmtFinType2': get_mapped_value('BsmtFinType2', BsmtFinType2),
        'BsmtUnfSF': apply_log(BsmtUnfSF),
        'TotalBsmtSF': float(TotalBsmtSF),
        '1stFlrSF': apply_log(stFlrSF),
        '2ndFlrSF': apply_log(ndFlrSF),
        'GrLivArea': apply_log(GrLivArea),
        'BsmtFullBath': apply_log(BsmtFullBath),
        'FullBath': float(FullBath),
        'KitchenQual': get_mapped_value('KitchenQual', KitchenQual),
        'Functional': get_mapped_value('Functional', Functional),
        'FireplaceQu': get_mapped_value('FireplaceQu', FireplaceQu),
        'GarageCars': float(GarageCars),
        'GarageQual': get_mapped_value('GarageQual', GarageQual),
        'GarageCond': get_mapped_value('GarageCond', GarageCond),
        'WoodDeckSF': apply_log(WoodDeckSF),
        'OpenPorchSF': apply_log(OpenPorchSF),
        'EnclosedPorch': apply_log(EnclosedPorch),
        'ScreenPorch': apply_log(ScreenPorch),
        'MoSold': float(MoSold),
        'Age': float(YrSold)-float(YearBuilt),
        'AgeRemod': float(YrSold)-float(YearRemodAdd),
        'AgeGarage': float(YrSold)-float(GarageYrBlt),
        'MSSubClass_class30': 1 if get_mapped_value('MSSubClass', MSSubClass) == 'class30' else 0,
        'MSSubClass_class40': 1 if get_mapped_value('MSSubClass', MSSubClass) == 'class40' else 0,
        'MSSubClass_class80': 1 if get_mapped_value('MSSubClass', MSSubClass) == 'class80' else 0,
        'MSSubClass_class85': 1 if get_mapped_value('MSSubClass', MSSubClass) == 'class85' else 0,
        'MSSubClass_class90': 1 if get_mapped_value('MSSubClass', MSSubClass) == 'class90' else 0,
        'MSZoning_RL': check_if_exist(MSZoning),
        'MSZoning_RM': check_if_exist(MSZoning),
        'LotConfig_FR2': check_if_exist(LotConfig),
        'Condition1_Norm': check_if_exist(Condition1),
        'Condition1_PosA': check_if_exist(Condition1),
        'Exterior1st_BrkFace': check_if_exist(Exterior1st),
        'Exterior1st_Plywood': check_if_exist(Exterior1st),
        'Foundation_Wood': check_if_exist(Foundation),
        'CentralAir_Y': 1 if CentralAir == 'Y' else 0,
        'GarageType_Detchd': check_if_exist(GarageType),
        'GarageFinish_Unf': check_if_exist(GarageFinish),
        'SaleType_ConLD': check_if_exist(SaleType),
        'SaleCondition_Normal': check_if_exist(SaleCondition)
    }

