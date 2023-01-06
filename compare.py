import ast
import argparse


def NormalizeText(text : str):
    parsing_tree = ast.parse(text)
    transformed_parse_tree = ast.NodeTransformer().visit(parsing_tree)
    return ast.unparse(transformed_parse_tree)


def LevenshteinDistance(first_text : str, second_text : str):
    dp_counter = list()
    for i in range(len(first_text)):
        dp_counter.append([0] * len(second_text))


    #base for dynamic
    for i in range(len(first_text)):
        dp_counter[i][0] = i
    for i in range(len(second_text)):
        dp_counter[0][i] = i



    for i in range(1, len(first_text)):
        for j in range(1, len(second_text)):
            is_differ  = (1 if first_text[i] != second_text[j] else 0)
            dp_counter[i][j] = min(dp_counter[i][j - 1] + 1,
                   dp_counter[i - 1][j] + 1,
                   dp_counter[i - 1][j - 1] + is_differ)

    return dp_counter[len(first_text) - 1][len(second_text) - 1]

def CountScores(input_file, output_file):
    scores = list()
    with open(input_file) as filename:
        pairs_to_compare = filename.readlines()
        for pairs in pairs_to_compare:
            current_pair = list(pairs.split())
            try:
                first = open(current_pair[0])
                first = NormalizeText(first.read())
                second = open(current_pair[1])
                second = NormalizeText(second.read())
                differ_dist = LevenshteinDistance(first, second)
                scores.append(1.0 - (differ_dist / max(len(first),
                len(second))))
            except:
                scores.append("This code has errors!")


    with open(output_file, "w") as filename:
        for i in range(len(scores)):
            filename.write(str(scores[i]) + "\n")


parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("output_file")
args = parser.parse_args()
print(args)
CountScores(args.input_file, args.output_file)
print(LevenshteinDistance("taxi", "taxrif"))
