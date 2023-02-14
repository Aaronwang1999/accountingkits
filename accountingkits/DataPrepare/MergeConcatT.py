import pandas as pd
import warnings


def mergelist_df(df_list, how, left_on, right_on, validate: str, **kwargs):
    """
    :param df_list: the dfs to be merged
    :param how: all of pd.merge()'s left_on option
    :param left_on: all of pd.merge()'s left_on option
    :param right_on: all of pd.merge()'s right_on option
    :param validate: all of pd.merge()'s concat option
    :param kwargs: all of pd.merge()'s other arguments,
    :return:
    """
    temp_df = df_list[0]
    for i in range(1, len(df_list)):
        temp_df = pd.merge(temp_df, df_list[i],
                           how=how, left_on=left_on, right_on=right_on, validate=validate,
                           **kwargs)
        if ((temp_df[left_on].nunique() != len(temp_df[left_on]))
                | (temp_df[left_on].nunique() != len(temp_df[right_on]))
        ):
            warnings.warn('not unique value imply X:m matching', SyntaxWarning)

    return temp_df

"""The Function has not passed the real test! We do not know the result!"""
# def merge_middlekey_df(left_df, right_df, middle_keys_df,
#                        left_on, right_on, middle_keys_left_on, middle_keys_right_on,
#                        how, validate):
#     """A Little Complex merge method:
#     left_df(left_on)<-
#         (middle_keys_left_on)middle_keys_df(middle_keys_right_on)
#                                             ->left_df(right_on)
#     how:pd.merge method
#     ARGUMENTS SHOULD BE STRING.
#     """
#     warnings.warn(
#         '\033[31mMergeConcatT.merge_middlekey_df has not passed the real test!\033[0m',
#         DeprecationWarning
#     )
#
#     if np.any(middle_keys_df.nunique(axis=0) != middle_keys_df.shape[1]):
#         raise ValueError("middle_keys_df seems duplicated, check again for matching")
#
#     if how == 'cross':
#         raise ValueError("Not Support Cartesian Cross merge Now")
#     elif how == 'left':
#         _temp_left_df = pd.merge(left_df, middle_keys_df,
#                                  left_on=left_on, right_on=middle_keys_left_on,
#                                  how='left', validate='many_to_one')
#         _temp_merge_df = pd.merge(_temp_left_df, right_df,
#                                   left_on=middle_keys_right_on, right_on=right_on,
#                                   how='left', validate=validate)
#     else:
#         _temp_right_df = pd.merge(middle_keys_df, right_df,
#                                   left_on=middle_keys_right_on, right_on=right_on,
#                                   how=how, validate='one_to_many')
#         _temp_merge_df = pd.merge(left_df, _temp_right_df,
#                                   left_on=left_on, right_on=middle_keys_left_on,
#                                   how=how, validate=validate)
#     return _temp_merge_df
