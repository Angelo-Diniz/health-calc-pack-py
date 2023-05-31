# test_health_calc_pack_py.py
import unittest

from health_calc_pack_py.imc import calcular_imc
from health_calc_pack_py.macronutrientes import calcular_macronutrientes, OBJETIVOS


class TestIMCMacronutrientes(unittest.TestCase):
    def test_calcular_imc(self):
        result = calcular_imc(70, 1.75)
        imc = result['IMC']
        self.assertAlmostEqual(imc, 22.86, delta=0.01)
    def test_calcular_macronutrientes_ganho_massa_muscular(self):
        resultado = calcular_macronutrientes(70, 1)
        self.assertEqual(resultado["Carboidratos"], 280)
        self.assertEqual(resultado["Proteinas"], 140)
        self.assertEqual(resultado["Gorduras"], 70)

    def test_calcular_macronutrientes_perda_gordura(self):
        resultado = calcular_macronutrientes(70, 2)
        self.assertEqual(resultado["Carboidratos"], 210)
        self.assertEqual(resultado["Proteinas"], 280)
        self.assertEqual(resultado["Gorduras"], 210)

    def test_calcular_macronutrientes_manutencao_peso(self):
        resultado = calcular_macronutrientes(70, 3)
        self.assertEqual(resultado["Carboidratos"], 280)
        self.assertEqual(resultado["Proteinas"], 280)
        self.assertEqual(resultado["Gorduras"], 140)

    def test_calcular_macronutrientes_perda_peso_ganho_massa_muscular(self):
        resultado = calcular_macronutrientes(70, 4)
        self.assertEqual(resultado["Carboidratos"], 245)
        self.assertEqual(resultado["Proteinas"], 105)
        self.assertEqual(resultado["Gorduras"], 70)

    def test_calcular_macronutrientes_objetivo_invalido(self):
        with self.assertRaises(ValueError):
            calcular_macronutrientes(70, 5)

    def test_calcular_macronutrientes_objetivo_descricao(self):
        for objetivo, descricao in OBJETIVOS.items():
            resultado_descricao = calcular_macronutrientes(70, descricao)
            resultado_numero = calcular_macronutrientes(70, objetivo)
            self.assertEqual(resultado_descricao, resultado_numero)

if __name__ == "__main__":
    unittest.main()
