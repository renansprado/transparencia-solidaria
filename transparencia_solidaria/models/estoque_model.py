from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from transparencia_solidaria.core.configs import settings

Base = settings.DBBaseModel


class Entidade(Base):
    """Entidade beneficente cadastrada no sistema."""

    __tablename__ = 'entidades'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(200), nullable=False)
    cidade: Mapped[str] = mapped_column(String(100), nullable=False)
    estado: Mapped[str] = mapped_column(String(2), nullable=False)
    telefone: Mapped[str | None] = mapped_column(String(20), nullable=True)
    criado_em: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    itens: Mapped[list['ItemEstoque']] = relationship('ItemEstoque', back_populates='entidade', lazy='select')

    def __repr__(self) -> str:
        return f'<Entidade id={self.id} nome={self.nome!r}>'


class ItemEstoque(Base):
    """Item de estoque vinculado a uma entidade."""

    __tablename__ = 'itens_estoque'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    entidade_id: Mapped[int] = mapped_column(Integer, ForeignKey('entidades.id', ondelete='CASCADE'), nullable=False)
    produto: Mapped[str] = mapped_column(String(200), nullable=False)
    categoria: Mapped[str] = mapped_column(String(100), nullable=False)
    quantidade_atual: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    quantidade_necessaria: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    unidade: Mapped[str] = mapped_column(String(20), nullable=False, default='kg')
    atualizado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    entidade: Mapped['Entidade'] = relationship('Entidade', back_populates='itens')

    @property
    def percentual_estoque(self) -> float:
        """Percentual preenchido em relação à necessidade (0–100)."""
        if self.quantidade_necessaria == 0:
            return 100.0
        return round((self.quantidade_atual / self.quantidade_necessaria) * 100, 1)

    @property
    def status(self) -> str:
        p = self.percentual_estoque
        if p < 25:
            return 'critico'
        if p < 60:
            return 'baixo'
        return 'adequado'

    def __repr__(self) -> str:
        return f'<ItemEstoque id={self.id} produto={self.produto!r}>'
