from marshmallow import fields, Schema


class ProdutoSchema(Schema):

    id = fields.Int()
    nome = fields.Str()
    marca = fields.Str()
    tipo = fields.Str()
    descricao = fields.Str()
    cod_barras = fields.Str(),
    preco_venda = fields.Float()
    preco_compra = fields.Float()
    medida = fields.Int()
    unidade = fields.Str()
    tags = fields.Str(many=True)
    unidade = fields.Str()
    data_cadastro = fields.Str()
    data_alteracao = fields.Str()
    ativo = fields.Bool()
