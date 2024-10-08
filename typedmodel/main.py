from loaddata import readlst, load_images, arrange_formulas
from cnn import model_config

if __name__ == "__main__":
    #load images and formulas for training
    image_names, render_types, formula_numbers = readlst(filename='data/im2latex_train.lst')
    train_formulas = arrange_formulas(formulafile='data/im2latex_formulas.lst', linenumbers=formula_numbers)
    train_images = load_images(foldername='data/fixed_formula_images/', filenames=image_names)
    print("[*] Loaded Training Images and Formulas")

    #load images and formulas for testing
    image_names, render_types, formula_numbers = readlst(filename='data/im2latex_test.lst')
    test_formulas = arrange_formulas(formulafile='data/im2latex_formulas.lst', linenumbers=formula_numbers)
    test_images = load_images(foldername='data/fixed_formula_images/', filenames=image_names)
    print("[*] Loaded Testing Images and Formulas")

    # possibly some form of normilization such as dividing each value 255.0

    model = ResNetModel.model_config()
    features = model.call(test_images)
    model.summary()
