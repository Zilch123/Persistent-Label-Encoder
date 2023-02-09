from sklearn.preprocessing import LabelEncoder

class PersistentLabelEncoder:
    def Label_Encoder_fit(df, categorical_features):
        """label encoder fit funtion, 
        Return label encoded DataFrame and encoder classes dict 

        Args:
            df (pandas dataframe): input to label encoder, 
            categorical_Features = ['f1', 'f2', ... 'fn']

        Returns:
            lbl_data- [dataframe]: label encoded values for training
            encoder_dict - [dict]: Dict of Labels classes_ 

        """
        
        lbl_data = df.copy()
        df_input = df[categorical_features].copy()
        enc = LabelEncoder()
        encoder_dict = dict()
        for cat in categorical_features:
            enc = enc.fit(list(df_input[cat]) + ['Unknown'])
            encoder_dict[cat] = [str(cat) for cat in enc.classes_]
            lbl_data[cat] = enc.transform(df_input[cat])
        return lbl_data, encoder_dict


    def label_encode_transform(df_infer, encoder, categorical_features):
        """Function used in Inference for Label encode transformation

        Args:
            df_infer (dataframe): input dataframe
            encoder (encoder dict pickle File Path): pickle file generated from Training

        Returns:
            df_infer [dataframe]: Label encoded DataFrame
        """

        lbl_input = df_infer[categorical_features].copy()
        encoder_dict = joblib.load(encoder)
        for cat in encoder_dict:
            for col in lbl_input.columns:
                le = LabelEncoder()
                if cat == col:
                    le.classes_ = encoder_dict[cat]
                    for unique_item in lbl_input[col].unique():
                        if unique_item not in le.classes_:
                            lbl_input[col] = ['Unknown' if x == unique_item else x for x in lbl_input[col]]
                    df_infer[col] = le.transform(lbl_input[col])
        return df_infer
