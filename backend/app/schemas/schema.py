from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.database import Base

class SACFormulario(Base):
    __tablename__ = "sac_formulario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    contato = Column(String)
    nota_fiscal = Column(String)
    assunto = Column(String)
    problema = Column(String)
    descricao = Column(Text)
    data_solicitado = Column(DateTime, server_default=func.now())
    arquivo = Column(String, nullable=True)
    itens = relationship(
        "SACItem",
        back_populates="formulario",
        cascade="all, delete-orphan"
    )
    
class SACItem(Base):
    __tablename__ = "sac_itens"
    
    id = Column(Integer, primary_key=True, index=True)
    formulario_id = Column(Integer, ForeignKey("sac_formulario.id"))
    nome_produto = Column(String)
    produto_id = Column(Integer)
    quantidade_original = Column(Integer)
    quantidade_devolucao = Column(Integer)
    formulario = relationship("SACFormulario", back_populates="itens")