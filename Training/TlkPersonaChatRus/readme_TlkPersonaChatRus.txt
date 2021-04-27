This file describes the data set TlkPersonaChatRus available at https://research.yandex.com/datasets/toloka.

The data set is intended for non-commercial use. You must indicate that the data was obtained using Yandex.Toloka. If you plan to use the datasets for commercial purposes, obtain consent from Yandex by contacting: toloka@support.yandex.com. 

This dataset of 10,000 dialogues will help researchers of dialogue systems to develop approaches for training chat bots. Prepared in collaboration with MIPT’s Neural Networks and Deep Learning Lab, the dataset contains profiles with a description of each individual's personality and dialogues between the research participants. A chatbot that is trained on the dataset will be able to communicate on behalf of a certain persona and get to know people by chatting with them on general topics.

Dialogs and profiles in HTML are in the file dialogues.tsv, the format is:
	<persona_1_profile>\t<persona_2_profile>\t<dialogue>
	Each dialog and profile is in HTML format.
Profiles are in the file profiles.tsv, the format is:
	<characteristic_1>\t<characteristic_2>\t<characteristic_3>\t<characteristic_4>\t<characteristic_5>

Some statistics about the dataset are below.
	The number of dialogs: 10013.
	The number of profiles: 1505.