from sklearn.preprocessing import LabelEncoder

class Encoder:
    def fit(df, categorical_features):
        """label encoder fit funtion, 
        Return label encoded DataFrame and encoder classes dict 

        Args:
            df (pandas dataframe): input to label encoder, 
            categorical_Features: List of column attributes E.g:['f1',...'fn']

        Returns:
            lbl_data- [dataframe]: label encoded values for training
            encoder_dict - [dict]: Dict of Labels classes_ 

        """
        
        lbl_data = df.copy()
        df_input = df[categorical_features].copy()
        enc = LabelEncoder()
        encoder_dict = dict()
        for cat in categorical_features:
            series = df_input[cat][df_input[cat].notnull()]
            series.loc[len(series)] = 'Unknown'
            enc = enc.fit(list(series), index=series.index)
            encoder_dict[cat] = [str(cat) for cat in enc.classes_]
            lbl_data[cat] = enc.transform(df_input[cat])
        return lbl_data, encoder_dict


    def transform(df_infer, encoder_dict, categorical_features, unknown_label = 'Unknown'):
        """Function used in Inference for Label encode transformation

        Args:
            df_infer (dataframe): input dataframe
            encoder (encoder dict): Encoder dict generated from Training

        Returns:
            df_infer [dataframe]: Label encoded DataFrame
        """

        lbl_input = df_infer[categorical_features].copy()
        for cat in encoder_dict:
            for col in lbl_input.columns:
                le = LabelEncoder()
                if cat == col:
                    le.classes_ = encoder_dict[cat]
                    for unique_item in lbl_input[col].unique():
                        if unique_item not in le.classes_:
                            lbl_input[col] = [unknown_label if x == unique_item else x for x in lbl_input[col]]
                    df_infer[col] = le.transform(lbl_input[col])
        return df_infer
