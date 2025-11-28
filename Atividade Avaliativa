
import java.util.Scanner;

public class PedidoLivro {
    
    // Enumeração que define todos os estados possíveis do DFA
    enum State { 
        SAUDACAO,           // Estado inicial, aguardando o comando para começar o pedido
        ESCOLHER_LIVRO,     // Aguardando a escolha do sabor
        ESCOLHER_VOLUME,   // Aguardando a escolha do tamanho da pizza
        ESCOLHER_AUTOR,    // Aguardando a escolha da bebida (ou se é "sem")
        INFORMAR_ENDERECO,  // Aguardando o endereço e telefone
        CONFIRMAR,          // Aguardando a confirmação, alteração ou cancelamento
        PAGAMENTO,          // Aguardando o método de pagamento
        FINALIZADO          // Pedido concluído, estado final
    }

    public static void main(String[] args) {
        // Inicializa o objeto Scanner para ler a entrada do console
        Scanner sc = new Scanner(System.in);
        
        // Define o estado inicial do DFA
        State state = State.SAUDACAO;
        
        // Variáveis para armazenar os dados do pedido (variáveis de contexto)
        String livro = null, volume = null, autor = null, endereco = null, pagamento = null;

        System.out.println("Bot: Olá! Diga 'quero pedir' para começar.");
        
        // Loop principal do DFA: continua executando até que o estado FINALIZADO ou CANCELADO seja atingido
        while (true) {
            // Lê, limpa e padroniza a entrada do usuário (para facilitar as verificações)
            String input = sc.nextLine().trim().toLowerCase();
            
            // Estrutura principal do DFA: a transição de estado é controlada pelo 'switch'
            switch (state) {
                
                // === ESTADO: SAUDACAO ===
                case SAUDACAO:
                    // Verifica se a entrada do usuário contém palavras-chave para iniciar o pedido.
                    // Isso é o critério de transição para o próximo estado.
                    if (input.contains("quero") || input.contains("pedir") || input.contains("livro") ) {
                        state = State.ESCOLHER_LIVRO; // Transição para o próximo estado
                        System.out.println("Bot: Qual o livro? (narnia, percy jackson, senhor dos aneis, hobbit)");
                    } else {
                        // Permanece no estado SAUDACAO
                        System.out.println("Bot: Diga 'quero pedir' quando quiser fazer um pedido.");
                    }
                    break;
                    
                // === ESTADO: ESCOLHER_LIVRO ===
                case ESCOLHER_LIVRO:
                    // Verifica qual dos sabores válidos foi mencionado na entrada
                    if (input.contains("narnia") || input.contains("senhor dos aneis") ||
                        input.contains("percy jackson") || input.contains("hobbit")) {
                        
                        // Determina e armazena o livro
                        if (input.contains("narnia")) livro = "narnia";
                        else if (input.contains("percy jackson")) livro = "percy jackson";
                        else if (input.contains("senhor dos aneis")) livro = "senhor dos aneis";
                        else livro = "hobbit";
                        
                        state = State.ESCOLHER_VOLUME; // Transição para o próximo estado
                        System.out.println("Bot: volume? (primeiro, segundo, terceiro)");
                    } else {
                        // Permanece no estado ESCOLHER_LIVRO
                        System.out.println("Bot: Não entendi. Escolha entre narnia, percy jackson, senhor dos aneis, hobbit.");
                    }
                    break;
                    
                // === ESTADO: ESCOLHER_VOLUME ===
                case ESCOLHER_VOLUME:
                    // Verifica e armazena o volume escolhido
                    if (input.contains("primeiro") || input.contains("primeira")) {
                        volume = "primeiro"; state = State.ESCOLHER_AUTOR;
                        System.out.println("Bot: Deseja dizer o nome do autor? (diga o nome ou 'sem')");
                    } else if (input.contains("segundo") || input.contains("segunda")) {
                        volume = "segundo"; state = State.ESCOLHER_AUTOR;
                        System.out.println("Bot: sabe o nome do autor? (diga o nome ou 'sem')");
                    } else if (input.contains("terceiro")) {
                        volume = "terceiro"; state = State.ESCOLHER_AUTOR;
                        System.out.println("Bot: sabe o nome do autor? (diga o nome ou 'sem')");
                    } else {
                        // Permanece no estado ESCOLHER_VOLUME
                        System.out.println("Bot: volume válidos: primeiro, segundo, terceiro.");
                    }
                    break;
                    
                // === ESTADO: ESCOLHER_AUTOR ===
                case ESCOLHER_AUTOR:
                    // Verifica se o usuário escolheu "sem autor"
                    if (input.contains("sem")) {
                        autor = "sem autor";
                    } else {
                        // Se não disse "sem", assume que a entrada é o nome da bebida.
                        // Nota: Esta lógica é simples e assume que a entrada é a bebida.
                        autor = input.isEmpty() ? "sem autor" : input;
                    }
                    state = State.INFORMAR_ENDERECO; // Transição
                    System.out.println("Bot: Informe endereço e telefone:");
                    break;
                    
                // === ESTADO: INFORMAR_ENDERECO ===
                case INFORMAR_ENDERECO:
                    // Validação simples: o endereço deve ter mais de 5 caracteres
                    if (input.length() > 5) {
                        endereco = input;
                        state = State.CONFIRMAR; // Transição para confirmação
                        
                        // Exibe o resumo do pedido
                        System.out.println("Bot: Confirma o pedido? (confirmar/alterar/cancelar)");
                        System.out.println("Resumo: " + livro + " (" + volume + ") - " + autor + " - " + endereco);
                    } else {
                        // Permanece no estado INFORMAR_ENDERECO
                        System.out.println("Bot: Endereço inválido. Informe rua, número e telefone.");
                    }
                    break;
                    
                // === ESTADO: CONFIRMAR ===
                case CONFIRMAR:
                    if (input.contains("confirm")) {
                        state = State.PAGAMENTO; // Transição para pagamento
                        System.out.println("Bot: Como deseja pagar? (dinheiro/cartão)");
                    } else if (input.contains("alter")) {
                        state = State.ESCOLHER_LIVRO; // Retorna para o início do processo (reset)
                        System.out.println("Bot: Ok, qual o novo livro?");
                    } else if (input.contains("cancel")) {
                        System.out.println("Bot: Pedido cancelado. Obrigado!");
                        sc.close(); return; // Sai do método, encerrando o programa
                    } else {
                        // Permanece no estado CONFIRMAR
                        System.out.println("Bot: Use confirmar, alterar ou cancelar.");
                    }
                    break;
                    
                // === ESTADO: PAGAMENTO ===
                case PAGAMENTO:
                    if (input.contains("din")) {
                        pagamento = "dinheiro"; state = State.FINALIZADO;
                    } else if (input.contains("cart")) {
                        pagamento = "cartão"; state = State.FINALIZADO;
                    } else {
                        // Permanece no estado PAGAMENTO
                        System.out.println("Bot: Escolha 'dinheiro' ou 'cartão'.");
                    }
                    
                    // Verifica se a transição para FINALIZADO ocorreu
                    if (state == State.FINALIZADO) {
                        System.out.println("Bot: Pedido confirmado! Resumo:");
                        System.out.println("livro: " + livro + " | volume: " + volume + " | autor: " + autor);
                        System.out.println("Endereço: " + endereco + " | Pagamento: " + pagamento);
                        System.out.println("Bot: Obrigado! Seu livro chegará em 3 dias.");
                        sc.close();
                        return; // Encerra o programa
                    }
                    break;
                    
                // === ESTADO: PADRAO/ERRO ===
                default:
                    // Caso um estado não mapeado seja atingido (erro de lógica)
                    System.out.println("Bot: Erro de estado.");
                    sc.close();
                    return;
            }
        }
    }
}
